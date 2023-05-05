"""
Methods for text parsing of source code
"""

from printer import *
from regexes import *
from methods import *
from method_header import *

def remove_comments(source):
    source = re.sub(ONE_LINE_COM_REG, "\n", source)
    source = re.sub(MULTI_LINE_COM_REG, "\n", source)
    return source

def get_code_of_method(name: str, source: str, source_len: int, endpos: int) -> str:
    """
    Find whole block of with potencial curly brackets inside 
    """
    depth = 1
    code = ""
    for i in range(endpos, source_len):
        c = source[i]
        if (c == "{"): depth += 1
        elif (c == "}"): 
            depth -= 1

        if (depth > 0): code += c
        else: break
    if (depth > 0):
        raise SyntaxError(f"Invalid block brackets in method '{name}'")
    return code


def prepare_methods(source: str, methods: dict) -> None:
    """
    Find all methods in source code and fill their
    code with respect to curly brackets inside
    """
    source_len = len(source)
    matches = re.findall(METHOD_FIND_REG, source)

    for match in matches:
        mtch = re.match(METHOD_REG, match)
        grp_dict = mtch.groupdict()

        endpos = source.find(match) + len(match)
        grp_dict["code"] = get_code_of_method(grp_dict["name"], source, source_len, endpos)

        key = generate_method_key(grp_dict)
        if (key in methods.keys()):
            raise SyntaxError(f"Duplicate method definition {key}({grp_dict['args_str']})")
        methods[key] = grp_dict
        methods[key]["key"] = key

def prepare_commands(sym_map: dict) -> None:
    """
    Split "code" of each method by ';' and build arg_header
    of method
    """
    methods = sym_map["methods"]
    for key in methods.keys():
        method = methods[key]
        method["commands"] = [i.strip() for i in method["code"].split(";")]
        while("" in method["commands"]):
            method["commands"].remove("")
        method["commands"].append("return")
        # build method header
        build_method_args(method, sym_map)

def translate_methods(sym_map: dict) -> None:
    methods = sym_map["methods"]
    for key in methods.keys():
        method = methods[key]
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