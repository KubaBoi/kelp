
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
    "CALL",
    "RET",
    "JMP",
    "JMC"
]

def build_alloc(var_name: str, size: int, sym_map: dict) -> list:
    """Build ALC instruction and return array of asm_code"""
    asm_code = []
    asm_code.append(INSTRUCTION_SET.index("ALC"))
    asm_code += get_variable_addr(var_name, sym_map)
    asm_code += to_256(size, SIZE_RANGE)
    return asm_code

def build_set(var_name: str, asm_bytes: list, sym_map: dict, offset = 0) -> list:
    """
    Build SET instruction and return array of asm_code
    
    Args:
        `asm_bytes` - list of integeres with values of bytes
    """
    asm_code = []
    asm_code.append(INSTRUCTION_SET.index("SET"))
    asm_code += get_variable_addr(var_name, sym_map)
    asm_code += to_256(offset, SIZE_RANGE) # offset
    asm_code += to_256(len(asm_bytes), SIZE_RANGE) # byte count
    asm_code += asm_bytes # value
    return asm_code

def build_cpt(dest_name: str, targ_name: str, sym_map: dict) -> list:
    """
    Build CPT isntruction and return array of asm_code
    """
    asm_code = []
    asm_code.append(INSTRUCTION_SET.index("CPT"))
    asm_code += get_variable_addr(dest_name, sym_map)
    asm_code += get_variable_addr(targ_name, sym_map)
    return asm_code

def build_cpy(dest_name: str, targ_name: str, byte_count: int, sym_map: dict) -> list:
    """
    Build CPY instruction and return array of asm_code
    """
    asm_code = []
    asm_code.append(INSTRUCTION_SET.index("CPY"))
    asm_code += to_256(byte_count, SIZE_RANGE)
    asm_code += get_variable_addr(dest_name, sym_map)
    asm_code += get_variable_addr(targ_name, sym_map)
    return asm_code

def build_call(method_key: str, args: list, method: dict, sym_map: dict) -> list:
    """
    Build CALL instruction and return array of asm_code

    Args:
        `method_key` - called method key

        `args` - list of names of variables as arguments for called method

        `method` - method object from where is call performed
    """
    asm_code = []
    asm_code.append(INSTRUCTION_SET.index("CALL"))
    asm_code.append(method_key)
    asm_code += [0 for i in range(1, ADDR_RANGE)] 
    for var_name in args:
        asm_code += get_variable_addr(var_name, sym_map)
    return asm_code

def build_return() -> list:
    return [INSTRUCTION_SET.index("RET")]

def build_jump(direction: bool, byte_count: int) -> list:
    """
    Build JMP instruction and return array of asm_code

    Args:
        `direction` - False-forwards, True-backwards

        `byte_count` - size of jump

        `method` - method object from where is call performed
    """
    asm_code = []
    asm_code.append(INSTRUCTION_SET.index("JMP"))
    asm_code += to_256(direction, 1)
    asm_code += to_256(byte_count, SIZE_RANGE)
    return asm_code