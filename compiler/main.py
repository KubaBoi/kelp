
import re

from config import *
from printer import *
from regexes import *
from source import *
from method_header import *
from methods import *
from cmd_regs import *
from assembly import *

script_path = "test.k"
byte_code_path = ".".join(script_path.split(".")[:-1])

with open(script_path, "r", encoding="utf-8") as f:
    source = f.read()

source = remove_comments(source)
methods = {}
"""
methods has `key`, 
- `key` key
- `name` name
- `args_str` which is string of args from source code
- `code` which is just str of body of method
- `args` which is array of arguments
    - items has `name` and `size`
- `commands` list of striped commands split by ';' from `code`
- `asm_code` list of instructions, mix of wannabe-bytes(1byte), 
    instruction names(1byte) and name of addresses(2byte)
    - every address for method will be 2 items in this list, first item is name
        and second one will be just 0 (it will help with calculating addresses) 
- `addr` value of address calculated during assembling
"""

sym_map = {
    "variable_count": 1, # because addr 0 is reserved for programm input
    "variables": {},
    "methods": methods
}
"""
variables has `method_name.name` (key)  
- `addr` as 2byte integer
- `size` integer
"""

try:
    prepare_methods(source, methods)
    prepare_commands(sym_map)
    translate_methods(sym_map)

    debug()
    byte_code = assemble(sym_map)
    debug()
except Exception as e:
    error(e)
    log("Aborting compilation.")
    exit(0)

if (DEBUG):
    for method_key in sym_map["methods"].keys():
        mth = sym_map["methods"][method_key]
        debug(f"[{mth['addr']} - {mth['name']}], ")
    debug()
    for key in sym_map["variables"].keys():
        var = sym_map["variables"][key]
        debug(f"{var['addr']} - {var['size']}B: {key}")

log()
log("Compilation successful :)")
log(f"Warning count: {len(printer_warns)}")
with open(byte_code_path, "wb") as f:
    f.write(byte_code)   
log(f"Bytecode generated into '{byte_code_path}'")