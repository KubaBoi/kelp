"""
Methods for single byte operations. 
"""

import re

from calc_256 import *
from regexes import *

ESCAPE_CHARS = {
    "\\": ord("\\"),
    "\'": ord("'"),
    "\"": ord("\""),
    "{": ord("{"),
    "}": ord("}"),
    "n": ord("\n"),
    "r": ord("\r"),
    "t": ord("\t"),
    "b": ord("\b"),
    "f": ord("\f"),
    "v": ord("\v"),
    "0": ord("\0")
}

def get_ord(char: str) -> int:
    """
    Return byte of character
    """
    if (len(char) == 1):
        return ord(char)
    if (char[1] not in ESCAPE_CHARS.keys()):
        raise SyntaxError(f"Escape character {char} does not exists or is not allowed")
    return ESCAPE_CHARS[char[1]]

def str_to_asm_bytes(value: str) -> list:
    """Convert string into asm_byte array"""
    chars = re.findall(SPLIT_TO_CHARS_REG, value)
    bytes = [get_ord(c) for c in chars]
    bytes.append(0)
    return bytes

def to_asm_bytes(value: list) -> list:
    """Convert list into asm_byte array"""
    bytes = []
    for val in value:
        val = val.strip()
        if (re.match(DEC_REG, val)):
            bytes += to_256(int(val), 1)
        elif (re.match(CHAR_REG, val)):
            val = val[1:-1] # remove ' from start and end
            bytes.append(get_ord(val))
    return bytes