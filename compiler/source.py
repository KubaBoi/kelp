"""
Methods for text parsing of source code
"""

from printer import *
from regexes import *
from methods import *
from method_header import *
from cmd_regs import *

def remove_comments(source):
    source = re.sub(ONE_LINE_COM_REG, "\n", source)
    source = re.sub(MULTI_LINE_COM_REG, "\n", source)
    return source

def get_block_code(grp_dict: dict, index: int, matches: list):
    depth = 1
    index += 1
    grp_dict["code"] = ""
    while (depth > 0 and index < len(matches)):
        grp_dict["code"] += matches[index]
        depth += len(re.findall(CRL_BRACK_0_REG, matches[index]))
        depth -= len(re.findall(CRL_BRACK_1_REG, matches[index]))
        index += 1
    if (depth > 0):
        raise SyntaxError("Missing block's code")            
    grp_dict["code"] = grp_dict["code"].strip()[:-1] # remove last }

def prepare_methods(source: str, methods: dict) -> None:
    """
    Find all methods in source code and fill their
    code with respect to curly brackets inside
    """
    matches = ["" if s == None else s.strip() for s in re.split(METHOD_SPLIT_REG, source)]
    while ("" in matches):
        matches.remove("")
    for m in matches:
        print(m.replace("\n", "\\n"))
    for i, match in enumerate(matches):
        mtch = re.match(METHOD_REG, match)
        if (mtch == None):
            continue
        grp_dict = mtch.groupdict()
        
        try:
            get_block_code(grp_dict, i, matches)
        except Exception as e:
            raise SyntaxError(e, f" at '{grp_dict['name']}({grp_dict['args_str']})'")
        print(grp_dict)
    
        key = generate_method_key(grp_dict)
        if (key in methods.keys()):
            raise SyntaxError(f"Duplicate method definition {key}({grp_dict['args_str']})")
        methods[key] = grp_dict
        methods[key]["key"] = key
        
def prepare_for_cycles(source: str):
    matches = ["" if s == None else s.strip() for s in re.split(FOR_CYCLE_SPLIT_REG, source)]
    while ("" in matches):
        matches.remove("")
    for m in matches:
        print(m.replace("\n", "\\n"))
    
    for i, match in enumerate(matches):
        mtch = re.match(METHOD_REG, match)
        if (mtch == None):
            continue
        grp_dict = mtch.groupdict()
        
        try:
            get_block_code(grp_dict, i, matches)
        except Exception as e:
            raise SyntaxError(e, f" at '{grp_dict['name']}({grp_dict['args_str']})'")
        
    

def prepare_commands(sym_map: dict) -> None:
    """
    Split "code" of each method by ';' and build arg_header
    of method
    """
    methods = sym_map["methods"]
    for key in methods.keys():
        method = methods[key]
        method["commands"] = [i.strip() for i in re.split(r";\s*\n|\Z", method["code"])]
        while ("" in method["commands"]):
            method["commands"].remove("")
        for i, cmd in enumerate(method["commands"]):
            if (cmd.endswith(";")):
                method["commands"][i] = cmd[:-1]
        method["commands"].append("return")
        # build method header
        build_method_args(method, sym_map)

def translate_methods(sym_map: dict) -> None:
    """
    Go throught all commands of every method and translate
    it to asm_code
    """
    methods = sym_map["methods"]
    for key in methods.keys():
        method = methods[key]
        debug(f"{key} ({method['args_str']}):")
        
        for cmd in method["commands"]:
            method["asm_code"] += translate_cmd(cmd, method, sym_map)
        debug(f"ASM: {method['asm_code']}")
    