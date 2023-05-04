
from calc_256 import *

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
    if (data["size"] == ""):
        data["size"] = 0

    name = create_name(data, method)
    if (name in sym_map["variables"].keys()):
        raise SyntaxError(f"Duplicated variable definition {name}")
    sym_map["variables"][name] = {}
    sym_map["variables"][name]["addr"] = to_256(sym_map["variable_count"], 2)
    sym_map["variables"][name]["size"] = int(data["size"])
    sym_map["variable_count"] += 1
    return name

def get_variable(data: dict, method: dict, sym_map: dict) -> dict:
    """
    Find variable in sym_map

    Raise:
        SyntaxError if variable does not exist

    Return:
        variable object
    """
    name = create_name(data, method)
    if (name not in sym_map["variables"].keys()):
        raise SyntaxError(f"Variable {name} was not defined")
    return sym_map["variables"][name]