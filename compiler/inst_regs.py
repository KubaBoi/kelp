
import re

from instruction_set import *
from calc_256 import *
from names import *
from escape_chars import *

class inst_reg:
    
    def __init__(self, reg: str) -> None:
        self.reg = re.compile(reg)

    def find_match(self, cmd: str) -> dict:
        matches = re.finditer(self.reg, cmd)
        for match in matches:
            return match.groupdict()
        
class raw_inst(inst_reg):
    def __init__(self, reg: str) -> None:
        super().__init__(reg)
        self.dec_reg = re.compile(r"^[0-9]+$")
        self.char_reg = re.compile(r"^'\\[a-z]{1}|.'$")
        self.str_reg = re.compile(r"^\"[.\n]*\"$")

    def find(self, cmd: str, method: dict, sym_map: dict) -> None:
        data = self.find_match(cmd)
        if (data == None):
            return
        return
        # TODO
        method["asm_code"].append(INSTRUCTION_SET.index(data["inst_name"].upper()))
        for arg in data["args"].split(" "):
            method["asm_code"].append(arg)    
        
    
class alloc(inst_reg):

    def __init__(self, reg: str) -> None:
        super().__init__(reg)

    def find(self, cmd: str, method: dict, sym_map: dict) -> None:
        data = self.find_match(cmd)
        if (data == None):
            return

        var_name = create_variable(data, method, sym_map)
        method["asm_code"].append(INSTRUCTION_SET.index("ALC"))
        method["asm_code"] += sym_map["variables"][var_name]["addr"]
        method["asm_code"] += to_256(int(data["size"]), 2) # size of alloc

class set_dec(inst_reg):

    def __init__(self, reg: str) -> None:
        super().__init__(reg)

    def find(self, cmd: str, method: dict, sym_map: dict) -> None:
        data = self.find_match(cmd)
        if (data == None):
            return
        
        var = get_variable(data, method, sym_map)
        method["asm_code"].append(INSTRUCTION_SET.index("SET"))
        method["asm_code"] += var["addr"]
        method["asm_code"] += to_256(0, 2) # offset
        method["asm_code"] += to_256(var["size"], 2) # byte count
        method["asm_code"] += to_256(int(data["value"]), var["size"]) # value

class set_char(inst_reg):

    def __init__(self, reg: str) -> None:
        super().__init__(reg)

    def find(self, cmd: str, method: dict, sym_map: dict) -> None:
        data = self.find_match(cmd)
        if (data == None):
            return
        
        var = get_variable(data, method, sym_map)
        method["asm_code"].append(INSTRUCTION_SET.index("SET"))
        method["asm_code"] += var["addr"]
        method["asm_code"] += to_256(0, 2) # offset
        method["asm_code"] += to_256(var["size"], 2) # byte count
        method["asm_code"] += to_256(get_ord(data["value"]), var["size"]) # value

class set_str(inst_reg):

    def __init__(self, reg: str) -> None:
        super().__init__(reg)

    def find(self, cmd: str, method: dict, sym_map: dict) -> None:
        data = self.find_match(cmd)
        if (data == None):
            return
        print("     ", data)

class set_bytes(inst_reg):

    def __init__(self, reg: str) -> None:
        super().__init__(reg)

    def find(self, cmd: str, method: dict, sym_map: dict) -> None:
        data = self.find_match(cmd)
        if (data == None):
            return
        print("     ", data)

inst_regs = {
    "raw_inst": raw_inst(r"^\$(?P<inst_name>[a-zA-Z]{2,4})\s+(?P<args>.*)"),
    "alloc": alloc(r"^byte(?P<size>[1-9]*)\s+(?P<var_name>[a-zA-Z0-9_]+)"),
    "set_dec": set_dec(r"(?P<var_name>[a-zA-Z0-9_]+)\s*=\s*(?P<value>[0-9]+)$"),
    "set_char": set_char(r"(?P<var_name>[a-zA-Z0-9_]+)\s*=\s*'(?P<value>\\[a-z]{1}|.)'$"),
    "set_str": set_str(r"(?P<var_name>[a-zA-Z0-9_]+)\s*=\s*\"(?P<value>[.\n]*)\"$"),
    "set_bytes": set_bytes(r"(?P<var_name>[a-zA-Z0-9_]+)\s*=\s*\{(?P<value>[.\n]*)\}$")
}