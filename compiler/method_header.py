
from inst_regs import inst_regs
from calc_256 import *
from names import *

class method_header_builder:

    @staticmethod
    def build_args(method: dict, sym_map: dict) -> None:
        """
        Prepare "asm_code" for method initialization and change `sym_map`

        Args:
            `method` - method object get from source code with regex

            `sym_map` - object about other variables
        """
        vars = method["args_str"].split(",")      
        method["asm_code"] = to_256(len(vars), 2)
        for var in vars:
            data = inst_regs["alloc"].find_match(var.strip())
            var_name = create_variable(data, method, sym_map)
            method["asm_code"] += sym_map["variables"][var_name]["addr"]
            