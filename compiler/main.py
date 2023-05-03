
import re

import instruction_set

with open("test.k", "r", encoding="utf-8") as f:
    source = f.read()

source = re.sub(r"//.+\n", "\n", source)
method_reg = re.compile(r"method\s+(?P<name>[a-zA-Z0-9_]+)\s*\((?P<args>[a-zA-Z0-9_,\s]+)\)\s*\{(?P<code>[\sa-zA-Z0-9,_\.\+\-\*;=/\\\(\)'\"\$]+)\}")

matches = re.finditer(method_reg, source)
methods = {}
for match in matches:
    grp_dict = match.groupdict()
    if (grp_dict["name"] in methods.keys()):
        print(f"Duplicate definition {grp_dict['name']}")
        continue
    methods[grp_dict["name"]] = grp_dict

for key in methods.keys():
    method = methods[key]
    method["not_byte_code"] = []
    method["commands"] = [i.strip() for i in method["code"].split(";")]
    while("" in method["commands"]):
        method["commands"].remove("")

    print(f"{key} ({method['args']}):")
    for cmd in method["commands"]:
        print(f"     {cmd}")

