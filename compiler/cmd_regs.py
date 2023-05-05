"""
Those classes are translators from source code to `asm_code`.

Methods search for its own regex pattern. If search return some data
those classes would generate kelp instructions as `asm_code`.

`asm_code` is like byte_code but addresses of methods are
only symbolic (after CALL or any JUMP instruction there would be
`method_key` as string in the `asm_code` array and next ADDR_RANGE - 1
bytes are 0s) and it is array of integers (not bytes - yet).

Those addresses would be changed after whole `asm_code` would be generated
and every method would have set address.
"""

import re

from printer import *
from instruction_set import *
from regexes import *
from calc_256 import *
from variables import *
from methods import *
from chars import *

class cmd_regex:
    def __init__(self, reg: str) -> None:
        self.reg = re.compile(reg)

    def find_match(self, cmd: str) -> dict:
        matches = re.finditer(self.reg, cmd)
        for match in matches:
            return match.groupdict()
    
class alloc(cmd_regex):
    def __init__(self) -> None:
        super().__init__(ALLOC_REG)

    def find(self, cmd: str, method: dict, sym_map: dict) -> bool:
        data = self.find_match(cmd)
        if (data == None):
            return False

        var_name = create_variable(data, method, sym_map)
        if (data["size"] == "0"):
            # should be array/string and then allocation is done there
            # or with ALC instruction
            return 
        method["asm_code"] += build_alloc(var_name, int(data["size"]), sym_map)
        return True
    
class raw_inst(cmd_regex):
    def __init__(self) -> None:
        super().__init__(RAW_INST_REG)

    def find(self, cmd: str, method: dict, sym_map: dict) -> bool:
        data = self.find_match(cmd)
        if (data == None):
            return False
    
        method["asm_code"].append(INSTRUCTION_SET.index(data["inst_name"].upper()))
        for arg in data["args"].split(" "):
            if (arg.isnumeric()):
                method["asm_code"] += to_256(int(arg))
            else:
                method["asm_code"] += get_variable_by_obj({"var_name": arg}, method, sym_map)["addr"]   
        return True

class set_dec(cmd_regex):
    def __init__(self) -> None:
        super().__init__(SET_DEC_REG)

    def find(self, cmd: str, method: dict, sym_map: dict) -> bool:
        data = self.find_match(cmd)
        if (data == None):
            return False
        
        var_name = create_name(data, method)
        var = get_variable_by_obj(data, method, sym_map)
        asm_bytes = to_256(int(data["value"]), var["size"])
        method["asm_code"] += build_set(var_name, asm_bytes, sym_map)
        return True

class set_char(cmd_regex):
    def __init__(self) -> None:
        super().__init__(SET_CHAR_REG)

    def find(self, cmd: str, method: dict, sym_map: dict) -> bool:
        data = self.find_match(cmd)
        if (data == None):
            return False
        
        var_name = create_name(data, method)
        asm_bytes = [get_ord(data["value"])]
        method["asm_code"] += build_set(var_name, asm_bytes, sym_map)
        return True

class set_str(cmd_regex):
    def __init__(self) -> None:
        super().__init__(SET_STR_REG)

    def find(self, cmd: str, method: dict, sym_map: dict) -> bool:
        data = self.find_match(cmd)
        if (data == None):
            return False
        
        var_name = create_name(data, method)
        var = get_variable(var_name, sym_map)
        asm_bytes = str_to_asm_bytes(data["value"])
        if (var["size"] == 0):
            var["size"] = len(asm_bytes)
            method["asm_code"] += build_alloc(var_name, len(asm_bytes), sym_map)
        elif (var["size"] < len(asm_bytes)):
            raise SyntaxError(f"Invalid size of string. Variable '{var_name}' is defined as {var['size']} byte(s) but set value is {len(asm_bytes)} characters long.")
        method["asm_code"] += build_set(var_name, asm_bytes, sym_map)
        return True
        
class set_bytes(cmd_regex):
    def __init__(self) -> None:
        super().__init__(SET_BYTES_REG)

    def find(self, cmd: str, method: dict, sym_map: dict) -> bool:
        data = self.find_match(cmd)
        if (data == None):
            return False
        
        var_name = create_name(data, method)
        var = get_variable(var_name, sym_map)
        asm_bytes = to_asm_bytes(data["value"].split(","))
        if (var["size"] == 0):
            var["size"] = len(asm_bytes)
            method["asm_code"] += build_alloc(var_name, len(asm_bytes), sym_map)
        elif (var["size"] < len(asm_bytes)):
            raise SyntaxError(f"Invalid size of array. Variable '{var_name}' is defined as {var['size']} byte(s) but set value is {len(asm_bytes)} characters long.")
        method["asm_code"] += build_set(var_name, asm_bytes, sym_map)
        return True

class cpt(cmd_regex):
    def __init__(self) -> None:
        super().__init__(CPT_REG)

    def find(self, cmd: str, method: dict, sym_map: dict) -> bool:
        data = self.find_match(cmd)
        if (data == None):
            return False
        
        dest_name = create_name({"var_name": data["dest"]}, method)
        targ_name = create_name({"var_name": data["targ"]}, method)
        dest = get_variable(dest_name, sym_map)
        targ = get_variable(targ_name, sym_map)
        dest["size"] = targ["size"]
        method["asm_code"] += build_cpt(dest_name, targ_name, sym_map)
        return True
        
class cpy(cmd_regex):
    def __init__(self) -> None:
        super().__init__(CPY_REG)

    def find(self, cmd: str, method: dict, sym_map: dict) -> bool:
        data = self.find_match(cmd)
        if (data == None):
            return False
        dest_name = create_name({"var_name": data["dest"]}, method)
        targ_name = create_name({"var_name": data["targ"]}, method)
        dest = get_variable(dest_name, sym_map)
        targ = get_variable(targ_name, sym_map)

        byte_count = dest["size"]
        if (dest["size"] != targ["size"]):
            warn(f"Destination '{dest_name}' ({dest['size']}B) and target '{targ_name}' ({targ['size']}B) are not the same size. May loss precision.")
            if byte_count > targ["size"]:
                byte_count = targ["size"] 
        method["asm_code"] += build_cpy(dest_name, targ_name, byte_count, sym_map)
        return True
        
class call(cmd_regex):
    def __init__(self) -> None:
        super().__init__(CALL_REG)

    def find(self, cmd: str, method: dict, sym_map: dict) -> bool:
        data = self.find_match(cmd)
        if (data == None):
            return False
        
        called_method = get_method(data, sym_map)
        args = [create_name_by_name(arg.strip(), method) for arg in data["args_str"].split(",")]
        
        for i, (arg, size) in enumerate(zip(args, called_method["args"])):
            var = get_variable(arg, sym_map)
            if (var["size"] != size and size != 0):
                warn(f"Call of method '{get_method_key_formatted(data)}' has different var size of {i}. arg - '{arg}':" +
                      f" Expected size is {size}B but provided is {var['size']}B")

        method["asm_code"] += build_call(called_method["key"], args, method, sym_map)
        return True

class rtrn(cmd_regex):
    def __init__(self) -> None:
        super().__init__(RTRN_REG)

    def find(self, cmd: str, method: dict, sym_map: dict) -> bool:
        data = self.find_match(cmd)
        if (data == None):
            return False
        
        method["asm_code"] += build_return()
        return True
    

CMD_REGEXES = {
    "alloc": alloc(),
    "raw_inst": raw_inst(),
    "set_dec": set_dec(),
    "set_char": set_char(),
    "set_str": set_str(),
    "set_bytes": set_bytes(),
    "cpt": cpt(),
    "cpy": cpy(),
    "call": call(),
    "return": rtrn()
}
"""Dict of functions which are able to decode commands"""