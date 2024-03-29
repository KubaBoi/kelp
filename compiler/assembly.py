"""
Methods for convertion from `asm_code` to `byte_code`
"""

from config import *
from printer import *
from calc_256 import *
from methods import *
from instruction_set import INSTRUCTION_SET
from dissasembly import *

def join_asm_code(sym_map: dict) -> list:
    """
    Join all `asm_codes` of all methods into one list
    and assign addresses to methods
    """
    asm_code = []
    asm_code += to_256(sym_map["variable_count"], SIZE_RANGE) # first SIZE_RANGE bytes for count of variables
    asm_code += to_256(INSTRUCTION_SET.index("CALL"), INST_RANGE) # first CALL instruction to call main
    asm_code.append("main_1")
    asm_code += to_256(0, ADDR_RANGE - 1) # address of program main function 
    asm_code += to_256(0, INST_RANGE) # KILL instruction after main call

    next_addr = len(asm_code)
    for method_key in sym_map["methods"].keys():
        method = sym_map["methods"][method_key]
        method["addr"] = next_addr
        asm_code += method["asm_code"]
        next_addr = len(asm_code)
    return asm_code

def replace_place_holders(asm_code: list, sym_map: dict) -> list:
    """
    Replace place holders to addresses of methods
    """
    debug(len(asm_code))
    for i, byte in enumerate(asm_code):
        if (not isinstance(byte, str)):
            continue
        method = get_method_by_key(byte, sym_map)
        addr = to_256(method["addr"], ADDR_RANGE)
        for o, v in enumerate(addr):
            asm_code[i + o] = v
    return asm_code


def assemble(sym_map: dict) -> bytes:
    """
    Generate byte_code
    """
    asm_code = join_asm_code(sym_map)
    asm_code = replace_place_holders(asm_code, sym_map)
    debug("[byte, index]")
    jumps = []
    for i, byte in enumerate(asm_code):
        if (byte == INSTRUCTION_SET.index("CALL")):
            jumps.append(asm_code[i+1])

    for i, byte in enumerate(asm_code):
        if (i in jumps):
            debug(f"\n[{byte}, {i}] ", end="")
        else:
            debug(f"{byte} ", end="")
    debug("\n")

    byte_code = b""
    for byte in asm_code:
        byte_code += byte.to_bytes(1, ENDIAN)

    if (not DEBUG):
        return byte_code
    
    method_addresses = []
    for method_key in sym_map["methods"].keys():
        method = sym_map["methods"][method_key]
        method_addresses.append(method["addr"])

    disass = dissasemble(byte_code, method_addresses)
    debug("*Skipping first 6 bytes")
    for d in disass:
        values = ""
        legend = ""
        for key in d.keys():
            if (key in ["index", "name", "size"]):
                continue
            values += f"{d[key]} "
            legend += f"{key}, "
        debug(f"{d['index']} - {d['name']} ({d['size']}B): {values} = {legend}")
        
    return byte_code
    
        