"""
Methods for searching in sym_map["methods"] and generating methods
`key`. 

`key` is unique id of every method. Its format is `method_name_<count_of_args>`. 
So methods can have multiple definitions but they need to have different 
count of arguments. 
"""

from calc_256 import *
from variables import *

def generate_method_key(method: dict) -> str:
    """
    Generate string in format :
    
    "method_name_<count_of_args>"

    and method["args"]
    """
    name = method["name"]
    args = method["args_str"].split(",")
    method["args"] = []
    for arg in args:
        type = arg.strip().split(" ")[0].replace("byte", "")
        if (type == ""):
            type = "0"
        method["args"].append(int(type))
    return f"{name}_{len(args)}"

def get_method_key(data: dict) -> dict:
    """
    Return key in format:

    "method_name_<count_of_args>"
    """
    name = data["method"]
    args = data["args_str"].split(",")
    return f"{name}_{len(args)}"

def get_method_key_formatted(data: dict) -> dict:
    """
    Return key in format:

    "method_name(<count_of_args> arguments)"
    """
    name = data["method"] + "("
    args = data["args_str"].split(",")
    return f"{name}({len(args)} arguments)"

def get_method(data: dict, sym_map: dict) -> dict:
    """
    Find method from sym_map

    Raise:
        SyntaxError if method does not exist
    """
    key = get_method_key(data)
    if (key not in sym_map["methods"].keys()):
        raise SyntaxError(f"Method {get_method_key_formatted(data)} was not defined")
    return sym_map["methods"][key]

def get_method_by_key(key: str, sym_map: dict) -> dict:
    """
    Find method from sym_map by `key`

    Raise:
        SyntaxError if method does not exist
    """
    if (key not in sym_map["methods"].keys()):
        raise SyntaxError(f"Method '{key}' was not defined")
    return sym_map["methods"][key]