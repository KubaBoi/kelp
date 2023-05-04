
from config import *
from calc_256 import *
from variables import *

INSTRUCTION_SET = [
    "KILL",
    "OUT",
    "SET",
    "CPT",
    "CPY",
    "ALC",
    "FRE",
    "RLC",
    "SUM",
    "SUB",
    "MUL",
    "DIV",
    "JMP",
    "JEQ",
    "JGE",
    "JLE",
    "JG",
    "JL",
    "CALL",
    "RET"
]

def build_alloc(var_name: str, size: int, sym_map: dict) -> list:
    """Build ALC instruction and return array of asm_code"""
    bytes = []
    bytes.append(INSTRUCTION_SET.index("ALC"))
    bytes += get_variable_addr(var_name, sym_map)
    bytes += to_256(size, SIZE_RANGE)
    return bytes

def build_set(var_name: str, asm_bytes: list, sym_map: dict, offset = 0) -> list:
    """
    Build SET instruction and return array of asm_code
    
    Args:
        `asm_bytes` - list of integeres with values of bytes
    """
    bytes = []
    bytes.append(INSTRUCTION_SET.index("SET"))
    bytes += get_variable_addr(var_name, sym_map)
    bytes += to_256(offset, SIZE_RANGE) # offset
    bytes += to_256(len(asm_bytes), SIZE_RANGE) # byte count
    bytes += asm_bytes # value
    return bytes

def build_call(method_key: str, args: list, method: dict, sym_map: dict) -> list:
    """
    Build CALL instruction and return array of asm_code

    Args:
        `method_key` - called method key

        `args` - list of names of variables as arguments for called method

        `method` - method object from where is call performed
    """
    bytes = []
    bytes.append(INSTRUCTION_SET.index("CALL"))
    bytes.append(method_key)
    bytes += [0 for i in range(1, ADDR_RANGE)] 
    for arg in args:
        arg = arg.strip()
        var_name = create_name({"var_name": arg}, method)
        bytes += get_variable_addr(var_name, sym_map)
    return bytes

def build_return() -> list:
    return [INSTRUCTION_SET.index("RET")]