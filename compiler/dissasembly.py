
from instruction_set import INSTRUCTION_SET
from calc_256 import *
from config import *

def build_dict(vals: list, *names):
    ret = {}
    for val, name in zip(vals, names):
        ret[name] = val
    if (len(vals) > len(names)):
        for i in range(len(names), len(vals)):
            ret[f"{names[-1]}{i+1}"] = vals[i]
    return ret

def get_byte_sequence(byte_code: bytes, sizes: list, index: int) -> tuple:
    values = []
    index += 1
    for sz in sizes:
        values.append(from_256(byte_code[index:index+sz]))
        index += sz
    return (index, values)    

class KILL:
    def get_inst(self, byte_code: bytes, index: int) -> tuple:
        """Return (index, {})"""
        return (index + 1, {})
    
class OUT:
    def get_inst(self, byte_code: bytes, index: int) -> tuple:
        """
        Return (index, dict)
        
        Return:
            `dict`: `{ "type": int, "addr": int }`
        """
        index, vals = get_byte_sequence(byte_code, [1, ADDR_RANGE], index)
        return (index, build_dict(vals, "type", "addr"))
        
class SET:
    def get_inst(self, byte_code: bytes, index: int) -> tuple:
        """
        Return (index, dict)

        Return:
            `dict`: `{ "addr": int, "offset": int, "byte_count": int, "bytes": [int] }`
        """
        index, vals = get_byte_sequence(byte_code, [ADDR_RANGE, SIZE_RANGE, SIZE_RANGE], index)
        bts = []
        for i in range(vals[2]):
            bts.append(byte_code[index])
            index += 1
        vals.append(bts)

        return (index, build_dict(vals, "addr", "offset", "byte_count", "bytes"))
    
class CPT:
    def get_inst(self, byte_code: bytes, index: int) -> tuple:
        """
        Return (index, dict)

        Return:
            `dict`: `{ "addr": int, "targ": int }`
        """
        index, vals = get_byte_sequence(byte_code, [ADDR_RANGE, ADDR_RANGE], index)
        return (index, build_dict(vals, "addr", "targ"))
    
class CPY:
    def get_inst(self, byte_code: bytes, index: int) -> tuple:
        """
        Return (index, dict)

        Return:
            `dict`: `{ "byte_count": int, "addr": int, "targ": int }`
        """
        index, vals = get_byte_sequence(byte_code, [SIZE_RANGE, ADDR_RANGE, ADDR_RANGE], index)
        return (index, build_dict(vals, "byte_count", "addr", "targ"))
    
class ALC:
    def get_inst(self, byte_code: bytes, index: int) -> tuple:
        """
        Return (index, dict)

        Return:
            `dict`: `{ "addr": int, "byte_count": int }`
        """
        index, vals = get_byte_sequence(byte_code, [ADDR_RANGE, SIZE_RANGE], index)
        return (index, build_dict(vals, "addr", "byte_count"))
    
class FRE:
    def get_inst(self, byte_code: bytes, index: int) -> tuple:
        """
        Return (index, dict)

        Return:
            `dict`: `{ "addr": int }`
        """
        index, vals = get_byte_sequence(byte_code, [ADDR_RANGE], index)
        return (index, build_dict(vals, "addr"))
    
class RLC:
    def get_inst(self, byte_code: bytes, index: int) -> tuple:
        """
        Return (index, dict)

        Return:
            `dict`: `{ "addr": int, "byte_count": int }`
        """
        index, vals = get_byte_sequence(byte_code, [ADDR_RANGE, SIZE_RANGE], index)
        return (index, build_dict(vals, "addr", "byte_count"))
    
class SUM:
    def get_inst(self, byte_code: bytes, index: int) -> tuple:
        """
        Return (index, dict)

        Return:
            `dict`: `{ "dest": int, "a": int, "b": int }`
        """
        index, vals = get_byte_sequence(byte_code, [ADDR_RANGE, ADDR_RANGE, ADDR_RANGE], index)
        return (index, build_dict(vals, "dest", "a", "b"))
    
class SUB:
    def get_inst(self, byte_code: bytes, index: int) -> tuple:
        """
        Return (index, dict)

        Return:
            `dict`: `{ "dest": int, "a": int, "b": int }`
        """
        index, vals = get_byte_sequence(byte_code, [ADDR_RANGE, ADDR_RANGE, ADDR_RANGE], index)
        return (index, build_dict(vals, "dest", "a", "b"))

class MUL:
    def get_inst(self, byte_code: bytes, index: int) -> tuple:
        """
        Return (index, dict)

        Return:
            `dict`: `{ "dest": int, "a": int, "b": int }`
        """
        index, vals = get_byte_sequence(byte_code, [ADDR_RANGE, ADDR_RANGE, ADDR_RANGE], index)
        return (index, build_dict(vals, "dest", "a", "b"))
    
class DIV:
    def get_inst(self, byte_code: bytes, index: int) -> tuple:
        """
        Return (index, dict)

        Return:
            `dict`: `{ "dest": int, "mod": int, "a": int, "b": int }`
        """
        index, vals = get_byte_sequence(byte_code, [ADDR_RANGE, ADDR_RANGE, ADDR_RANGE, ADDR_RANGE], index)
        return (index, build_dict(vals, "dest", "mod", "a", "b"))
    
class CALL:
    def get_inst(self, byte_code: bytes, index: int) -> tuple:
        """
        Return (index, dict)

        Return:
            `dict`: `{ "dest": int, "arg...n": int }`
        """
        index, vals = get_byte_sequence(byte_code, [ADDR_RANGE], index)
        i, args = get_byte_sequence(byte_code, [SIZE_RANGE], vals[0]-1)
        for arg_ind in range(args[0]):
            index, vls = get_byte_sequence(byte_code, [ADDR_RANGE], index-1)
            vals.append(vls[0])
        return (index, build_dict(vals, "dest", "arg"))
    
class RET:
    def get_inst(self, byte_code: bytes, index: int) -> tuple:
        """
        Return (index, {})
        """
        return (index + 1, {})
        
class JMP:
    def get_inst(self, byte_code: bytes, index: int) -> tuple:
        """
        Return (index, dict)

        Return:
            `dict`: { "direction": int, "jump_size": int }
        """
        index, vals = get_byte_sequence(byte_code, [1, SIZE_RANGE], index)
        return (index, build_dict(vals, "direction", "jump_size"))    
    
class JMC:
    def get_inst(self, byte_code: bytes, index: int) -> tuple:
        """
        Return (index, dict)

        Return:
            `dict`: { "condition": int, "jump_size": int, "arg0": int, "arg1": int }
        """
        index, vals = get_byte_sequence(byte_code, [1, SIZE_RANGE, ADDR_RANGE, ADDR_RANGE], index)
        return (index, build_dict(vals, "direction", "jump_size", "arg0", "arg1"))    
    
DISSASEMBLE_INSTRUCTIONS = [KILL(), OUT(), SET(), CPT(), CPY(), ALC(), FRE(), RLC(),
                            SUM(), SUB(), MUL(), DIV(), CALL(), RET(), JMP(), JMC()]

def dissasemble(byte_code: bytes, method_addresses = None) -> list:
    """
    Dissasemble `byte_code`, if `method_addresses` is None then it will
    try to create this list, but need to mention, that this process will be 
    disrupted by bytes that are the same value as CALL but are not this 
    instruction.
    """
    if (method_addresses == None):
        method_addresses = []
        for i in range(len(byte_code[2:])):
            byte = byte_code[i]
            if (byte == INSTRUCTION_SET.index("CALL")):
                method_addresses.append(from_256(byte_code[i+1:i+1+ADDR_RANGE]))

    index = 6
    dcts = []
    while index < len(byte_code) - 1:
        index_old = index
        if (index in method_addresses): # method
            dct = [index]
            index, args = get_byte_sequence(byte_code, [2], index - 1)
            dct += args
            for i in range(args[0]):
                index, val = get_byte_sequence(byte_code, [2], index - 1)
                dct += val
            dct = build_dict(dct, "index", "arg_count", "arg")
            #print("METHOD_HEADER", dct)
            dct["name"] = "METHOD_HEADER"
        else:
            inst = DISSASEMBLE_INSTRUCTIONS[byte_code[index]]
            name = INSTRUCTION_SET[byte_code[index]]
            index, dct = inst.get_inst(byte_code, index)
            #print(name, dct)
            dct["name"] = name
        dct["index"] = index_old
        dct["size"] = index - index_old
        dcts.append(dct)
    return dcts