
import re

from config import *
from printer import *
from regexes import *
from method_header import *
from methods import *
from cmd_regs import *
from assembly import *

script_path = "test.k"
byte_code_path = ".".join(script_path.split(".")[:-1])

with open(script_path, "r", encoding="utf-8") as f:
    source = f.read()

source = re.sub(ONE_LINE_COM_REG, "\n", source)
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

"""
def iter(txt, itr = 0):
    code = "{"
    blocks = []
    while itr < len(txt) and txt[itr] != "}":
        if (txt[itr] == "{"):
            itr, new_code, new_blocks = iter(txt, itr + 1)
            blocks.append({
                "code": new_code,
                "blocks": new_blocks
            })
        code += txt[itr]
        itr += 1
    return itr, code + "}", blocks
    
i, code, blocks = iter(source)
print(i, code, blocks)
"""


matches = re.finditer(METHOD_REG, source)
try:
    for match in matches:
        grp_dict = match.groupdict()
        key = generate_method_key(grp_dict)
        if (key in methods.keys()):
            raise SyntaxError(f"Duplicate method definition {key}({grp_dict['args_str']})")
        methods[key] = grp_dict
        methods[key]["key"] = key

    for key in methods.keys():
        method = methods[key]
        method["commands"] = [i.strip() for i in method["code"].split(";")]
        while("" in method["commands"]):
            method["commands"].remove("")
        method["commands"].append("return")
        build_method_args(method, sym_map)

        debug(f"{key} ({method['args_str']}):")
        for cmd in method["commands"]:
            found = False
            for key in CMD_REGEXES.keys():
                inst_obj = CMD_REGEXES[key]
                if (inst_obj.find(cmd, method, sym_map)):
                    found = True
                    if (key != "alloc"):
                        break
            if (not found):
                raise SyntaxError(f"Cannot translate command: '{cmd}'")

        debug(f"ASM: {method['asm_code']}")

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