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
        
class raw_inst(cmd_regex):
    def __init__(self) -> None:
        super().__init__(RAW_INST_REG)

    def find(self, cmd: str, method: dict, sym_map: dict) -> None:
        data = self.find_match(cmd)
        if (data == None):
            return
    
        method["asm_code"].append(INSTRUCTION_SET.index(data["inst_name"].upper()))
        for arg in data["args"].split(" "):
            if (arg.isnumeric()):
                method["asm_code"] += to_256(int(arg))
            else:
                method["asm_code"] += get_variable_by_obj({"var_name": arg}, method, sym_map)["addr"]   
        
    
class alloc(cmd_regex):

    def __init__(self) -> None:
        super().__init__(ALLOC_REG)

    def find(self, cmd: str, method: dict, sym_map: dict) -> None:
        data = self.find_match(cmd)
        if (data == None):
            return

        var_name = create_variable(data, method, sym_map)
        if (data["size"] == "0"):
            # should be array/string and then allocation is done there
            # or with ALC instruction
            return 
        method["asm_code"] += build_alloc(var_name, int(data["size"]), sym_map)

class set_dec(cmd_regex):

    def __init__(self) -> None:
        super().__init__(SET_DEC_REG)

    def find(self, cmd: str, method: dict, sym_map: dict) -> None:
        data = self.find_match(cmd)
        if (data == None):
            return
        
        var_name = create_name(data, method)
        var = get_variable_by_obj(data, method, sym_map)
        asm_bytes = to_256(int(data["value"]), var["size"])
        method["asm_code"] += build_set(var_name, asm_bytes, sym_map)

class set_char(cmd_regex):

    def __init__(self) -> None:
        super().__init__(SET_CHAR_REG)

    def find(self, cmd: str, method: dict, sym_map: dict) -> None:
        data = self.find_match(cmd)
        if (data == None):
            return
        
        var_name = create_name(data, method)
        asm_bytes = [get_ord(data["value"])]
        method["asm_code"] += build_set(var_name, asm_bytes, sym_map)

class set_str(cmd_regex):

    def __init__(self) -> None:
        super().__init__(SET_STR_REG)

    def find(self, cmd: str, method: dict, sym_map: dict) -> None:
        data = self.find_match(cmd)
        if (data == None):
            return
        
        var_name = create_name(data, method)
        var = get_variable(var_name, sym_map)
        asm_bytes = str_to_asm_bytes(data["value"])
        if (var["size"] == 0):
            method["asm_code"] += build_alloc(var_name, len(asm_bytes), sym_map)
        elif (var["size"] < len(asm_bytes)):
            raise SyntaxError(f"Invalid size of string. Variable '{var_name}' is defined as {var['size']} byte(s) but set value is {len(asm_bytes)} characters long.")
        method["asm_code"] += build_set(var_name, asm_bytes, sym_map)
        
class set_bytes(cmd_regex):

    def __init__(self) -> None:
        super().__init__(SET_BYTES_REG)

    def find(self, cmd: str, method: dict, sym_map: dict) -> None:
        data = self.find_match(cmd)
        if (data == None):
            return
        
        var_name = create_name(data, method)
        var = get_variable(var_name, sym_map)
        asm_bytes = to_asm_bytes(data["value"].split(","))
        if (var["size"] == 0):
            method["asm_code"] += build_alloc(var_name, len(asm_bytes), sym_map)
        elif (var["size"] < len(asm_bytes)):
            raise SyntaxError(f"Invalid size of array. Variable '{var_name}' is defined as {var['size']} byte(s) but set value is {len(asm_bytes)} characters long.")
        method["asm_code"] += build_set(var_name, asm_bytes, sym_map)

class call(cmd_regex):

    def __init__(self) -> None:
        super().__init__(CALL_REG)

    def find(self, cmd: str, method: dict, sym_map: dict) -> None:
        data = self.find_match(cmd)
        if (data == None):
            return
        
        # TODO different types warning
        called_method = get_method(data, sym_map)
        args = data["args_str"].split(",")
        method["asm_code"] += build_call(called_method["key"], args, method, sym_map)
        
class rtrn(cmd_regex):
    def __init__(self) -> None:
        super().__init__(RTRN_REG)

    def find(self, cmd: str, method: dict, sym_map: dict) -> None:
        data = self.find_match(cmd)
        if (data == None):
            return
        
        method["asm_code"] += build_return()
    

CMD_REGEXES = {
    "raw_inst": raw_inst(),
    "alloc": alloc(),
    "set_dec": set_dec(),
    "set_char": set_char(),
    "set_str": set_str(),
    "set_bytes": set_bytes(),
    "call": call(),
    "return": rtrn()
}
"""Dict of functions which are able to decode commands"""