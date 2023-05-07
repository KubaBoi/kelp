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

def get_block_code(grp_dict: dict, index: int, matches: list) -> int:
    """
    Go throught all block matches and join commands
    which belongs a block

    This method will join only level 1 blocks...

    for code:
    
    ```
    for (...)
    {
        for (...) {}
    }
    ``` 

    The second one for cycle will be saved as whole string with other commands
    in dictionary object of first one cycle

    Return:
        `new index` and into `grp_dict` will be added "code" key 
    """
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
    splt = grp_dict["code"].split("}")   
    matches[index - 1] = splt[-1]         
    grp_dict["code"] = "}".join(splt[:-1])
    return index - 1

def prepare_methods(source: str, methods: dict) -> None:
    """
    Find all methods in source code and fill their
    code with respect to curly brackets inside
    """
    matches = ["" if s == None else s.strip() for s in re.split(METHOD_SPLIT_REG, source)]
    while ("" in matches):
        matches.remove("")
        
    i = 0
    while i < len(matches):
        mtch = re.match(METHOD_REG, matches[i])
        if (mtch == None):
            i += 1
            continue
        grp_dict = mtch.groupdict()
        
        try:
            i = get_block_code(grp_dict, i, matches)
        except Exception as e:
            raise SyntaxError(e, f" at '{grp_dict['name']}({grp_dict['args_str']})'")
    
        key = generate_method_key(grp_dict)
        if (key in methods.keys()):
            raise SyntaxError(f"Duplicate method definition {key}({grp_dict['args_str']})")
        methods[key] = grp_dict
        methods[key]["key"] = key
        
def prepare_block(source: str, type: str, split_reg, match_reg) -> dict:
    """
    Prepare one block (it will take all commands and other blocks)
    and return it as dictionary with "code", "type", "args_str" and "args"
    where "args" is list of commands parsed from "args_str"
    """
    matches = ["" if s == None else s.strip() for s in re.split(split_reg, source)]
    data = []
    while ("" in matches):
        matches.remove("")
    
    i = 0
    while i < len(matches):
        mtch = re.match(match_reg, matches[i])
        if (mtch == None):
            data.append(matches[i])
            i += 1
            continue
        grp_dict = mtch.groupdict()
        grp_dict["type"] = type
        
        try:
            i = get_block_code(grp_dict, i, matches)
        except Exception as e:
            raise SyntaxError(e, f" at 'for cycle'")
        data.append(grp_dict)
    return data 

def prepare_blocks(code: str) -> list:
    """
    Prepare all inside blocks of one block recursively
    and return list of commands
    """
    block_data = prepare_block(code, 0, FOR_CYCLE_SPLIT_REG, FOR_CYCLE_REG) 
        
    commands = []
    for block in block_data:
        if (isinstance(block, str)):
            commands += [bl.strip() for bl in block.split(";")]
        else:
            block["args"] = [arg.strip() for arg in block["args_str"].split(";")]
            while "" in block["args"]:
                block["args"].remove("")
            block["commands"] = prepare_blocks(block["code"])
            commands.append(block)
    while ("" in commands):
        commands.remove("")
    return commands

def translate_condition(cmd: str, method: dict) -> dict:
    """
    Translate condition

    Args:
        `cmd` - string of condition, for example `arg0 < arg1`

    Return:
        dictionary with `arg0` and `arg1` (var_name) and `operator` (number)
        
        for completing condition type, `operator` need to be multiplied
        by 2 and add 0 or 1 (0-forwards, 1-backwards)
    """
    mtch = re.match(CONDITION_REG, cmd)
    if (mtch == None):
        raise SyntaxError(f"There need to be proper condition in '{method['name']}'")
    arg0_var_name = create_name_by_name(mtch["arg0"], method)
    arg1_var_name = create_name_by_name(mtch["arg1"], method)
    operator = CONDITION_SET.index(mtch["operator"])
    if (operator < 0):
        raise SyntaxError(f"Invalid operator '{mtch['operator']}'")
    return {
        "arg0": arg0_var_name,
        "arg1": arg1_var_name,
        "operator": operator
    }
    

def custom_command(command: dict, method: dict, sym_map: dict) -> list:
    """
    Resucrsion
    """
    asm_code = []
    args = command["args"]
    if (command["type"] == 0): # for cycle
        asm_code += translate_cmd(args[0], method, sym_map) # iterator init
        before_size = len(asm_code)
        asm_code += translate_commands(command["commands"], method, sym_map) # code inside
        asm_code += translate_cmd(args[2], method, sym_map) # iterator change
        condition = translate_condition(args[1], method)
        cond_type = condition["operator"] * 2 + 1
        asm_code += build_jump_conditional(
            cond_type, 
            len(asm_code) - before_size + 6, 
            condition["arg0"],
            condition["arg1"],
            sym_map
        )
    return asm_code


def translate_commands(commands: list, method: dict, sym_map: dict) -> list:
    """
    From list of commands (str | dict) creates `asm_code`
    and return it
    """
    asm_code = []
    for cmd in commands:
        if (isinstance(cmd, str)):
            asm_code += translate_cmd(cmd, method, sym_map)
            continue
        asm_code += custom_command(cmd, method, sym_map)
    return asm_code

def prepare_commands(sym_map: dict) -> None:
    """
    Split "code" of each method by ';' and build arg_header
    of method
    """
    methods = sym_map["methods"]
    for key in methods.keys():
        method = methods[key]

        method["commands"] = prepare_blocks(method["code"])
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
        method["asm_code"] += translate_commands(method["commands"], method, sym_map)
        debug(f"ASM: {method['asm_code']}")
    