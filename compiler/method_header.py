
from config import *
from cmd_regs import CMD_REGEXES
from calc_256 import *
from variables import *

def build_method_args(method: dict, sym_map: dict) -> None:
    """
    Prepare "asm_code" for method initialization and change `sym_map`

    Args:
        `method` - method object get from source code with regex

        `sym_map` - object about other variables
    """
    vars = method["args_str"].split(",")      
    method["asm_code"] = to_256(len(vars), SIZE_RANGE)

    # first address is reserved for program input
    if (method["name"] == "main"):
        method["asm_code"] += to_256(0, ADDR_RANGE)
        var_name = create_input_ptr(method, sym_map)
        return

    for var in vars:
        data = CMD_REGEXES["alloc"].find_match(var.strip())
        var_name = create_variable(data, method, sym_map)
        method["asm_code"] += sym_map["variables"][var_name]["addr"]