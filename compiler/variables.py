"""
Methods for searching and creating variables in sym_map["variables"].

`variable is created` means just that compiler knows about its
keyword. But it does not generatey any `asm_code`.

This is used for variables with optional data type.

`byte string;` - compiler knows about it, so final program will have space in `mem` 
for this variable but it could not be even allocated.
"""

from config import *
from calc_256 import *

def create_input_ptr(method: dict, sym_map: dict) -> str:
    split_args = method["args_str"].split(",")
    if (len(split_args) != 1):
        raise SyntaxError("There need to be exactly 1 argument in 'main' function.")
    type_name = split_args[0].split(" ")
    if (len(type_name) != 2):
        raise SyntaxError("Syntax in main header.")
    name = type_name[1]
    # compiler does not care about users data type
    # it will always be `byte`
    sym_map["variables"][name] = {}
    sym_map["variables"][name]["addr"] = to_256(0, ADDR_RANGE)
    sym_map["variables"][name]["size"] = 0
    return name

def create_name(data: dict, method: dict) -> str:
    return f"{method['name']}.{data['var_name']}"

def create_variable(data: dict, method: dict, sym_map: dict) -> str:
    """
    Build name for sym_map in "method_name.var_name" format

    Method will create item in sym_map and add 1 to "variable_count"

    Args:
        `data` - object returned by find_match with alloc regex

    Raise:
        SyntaxError if variable with this name already exists
    """
    data["size"] = "0" + data["size"]

    name = create_name(data, method)
    if (name in sym_map["variables"].keys()):
        raise SyntaxError(f"Duplicated variable definition {name}")
    sym_map["variables"][name] = {}
    sym_map["variables"][name]["addr"] = to_256(sym_map["variable_count"], ADDR_RANGE)
    sym_map["variables"][name]["size"] = int(data["size"])
    sym_map["variable_count"] += 1
    return name

def get_variable_by_obj(data: dict, method: dict, sym_map: dict) -> dict:
    """
    Find variable in sym_map

    Raise:
        SyntaxError if variable does not exist

    Return:
        variable object
    """
    name = create_name(data, method)
    return get_variable(name, sym_map)

def get_variable_addr(var_name: str, sym_map: dict) -> list:
    """Find variable in sym_map and return its address"""
    return get_variable(var_name, sym_map)["addr"]

def get_variable(var_name: str, sym_map: dict) -> dict:
    """
    Find variable in sym_map

    Raise:
        SyntaxError if variable does not exist

    Return:
        variable object
    """
    if (var_name not in sym_map["variables"].keys()):
        raise SyntaxError(f"Variable {var_name} was not defined")
    return sym_map["variables"][var_name]