
import re

import instruction_set
from method_header import *
from inst_regs import *


with open("test.k", "r", encoding="utf-8") as f:
    source = f.read()

source = re.sub(r"//.+\n", "\n", source)
# TODO opravit tenhle regex aby code byl pro vsechny znaky
method_reg = re.compile(r"method\s+(?P<name>[a-zA-Z0-9_]+)\s*\((?P<args_str>[a-zA-Z0-9_,\s]+)\)\s*\{(?P<code>[\sa-zA-Z0-9,_\.\+\-\*;=/\\\(\)'\"\$\?]*)\}")

"""
methods has "name"(key), 
- "name" there is name inside
- "args_str" which is string of args from source code
- "code" which is just str of body of method
- "args" which is array of arguments
    - items has "name" and "size"
- "commands" list of striped commands split by ';' from "code"
- "asm_code" list of instructions, mix of wannabe-bytes(1byte), 
    instruction names(1byte) and name of addresses(2byte)
    - every address for method will be 2 items in this list, first item is name
        and second one will be just 0 (it will help with calculating addresses) 
"""
methods = {}

"""
variables has "method_name.name"(key)  
- "addr" as 2byte integer
- "size" integer
"""
sym_map = {
    "variable_count": 0,
    "variables": {}
}

matches = re.finditer(method_reg, source)
for match in matches:
    grp_dict = match.groupdict()
    grp_name = grp_dict["name"]
    if (grp_name in methods.keys()):
        raise SyntaxError(f"Duplicate method definition {grp_name}({grp_dict['args_str']})")
    methods[grp_name] = grp_dict

for key in methods.keys():
    method = methods[key]
    method["commands"] = [i.strip() for i in method["code"].split(";")]
    while("" in method["commands"]):
        method["commands"].remove("")
    method_header_builder.build_args(method, sym_map)

    print(f"{key} ({method['args_str']}):")
    for cmd in method["commands"]:
        for key in inst_regs.keys():
            inst_obj = inst_regs[key]
            inst_obj.find(cmd, method, sym_map)
    print(f"ASM: {method['asm_code']}")

for key in sym_map["variables"].keys():
    var = sym_map["variables"][key]
    print(key, var["addr"], var["size"])

