"""
All precompiled regexes used in compiler
"""

import re

METHOD_FIND_REG = re.compile(r"method\s+[a-zA-Z0-9_]+\s*\([a-zA-Z0-9_,\s]+\)\s*\{")
METHOD_REG = re.compile(r"method\s+(?P<name>[a-zA-Z0-9_]+)\s*\((?P<args_str>[a-zA-Z0-9_,\s]+)\)\s*\{")

DEC_REG = re.compile(r"^(?P<value>[0-9]+)$")
CHAR_REG = re.compile(r"^'(?P<value>\\[\\'\"\{\}0nrtfbv]{1}|.)'$")
STR_REG = re.compile(r"^\"(?P<value>[.\n]*)\"$")

SPLIT_TO_CHARS_REG = re.compile(r"\\[\\'\"\{\}0nrtfbv]{1}|.")

ONE_LINE_COM_REG = re.compile(r"//.+\n")
MULTI_LINE_COM_REG = re.compile(r"\/\*[\w\W\s]*?\*\/")

# COMMANDS
RAW_INST_REG = re.compile(r"^\$(?P<inst_name>[a-zA-Z]{2,4})\s+(?P<args>.*)")
ALLOC_REG = re.compile(r"^byte(?P<size>[1-9]*)\s+(?P<var_name>[a-zA-Z0-9_]+)")
SET_DEC_REG = re.compile(r"(?P<var_name>[a-zA-Z0-9_]+)\s*=\s*(?P<value>[0-9]+)$")
SET_CHAR_REG = re.compile(r"(?P<var_name>[a-zA-Z0-9_]+)\s*=\s*'(?P<value>\\[a-z]{1}|.)'$")
SET_STR_REG = re.compile(r"(?P<var_name>[a-zA-Z0-9_]+)\s*=\s*\"(?P<value>[\s\w\W]*)\"$")
SET_BYTES_REG = re.compile(r"(?P<var_name>[a-zA-Z0-9_]+)\s*=\s*\[(?P<value>[\s\w\W]*)\]$")
CPT_REG = re.compile(r"(?P<dest>[a-zA-Z0-9_]+)\s*=\s*(?P<targ>[a-zA-Z0-9_]+)")
CPY_REG = re.compile(r"(?P<dest>[a-zA-Z0-9_]+)\s*=\s*\*\s*(?P<targ>[a-zA-Z0-9_]+)")
CALL_REG = re.compile(r"(?P<method>[a-zA-Z0-9_]+)\((?P<args_str>[a-zA-Z0-9_,\s]+)\)")
RTRN_REG = re.compile(r"^return$")

# CODE STRUCTURES
FOR_FIND_REG = re.compile(r"for\s*\(\s*byte[0-9]*\s+[a-zA-Z0-9_]+\s*=\s*[0-9]+;\s*[^;]+;\s*[^;]+\s*\)\s*\{")
FOR_REG = re.compile(r"for\s*\(\s*byte(?P<iter_size>[0-9]*)\s+(?P<iter_name>[a-zA-Z0-9_]+)\s*=\s*(?P<value>[0-9]+);\s*(?P<condition>[^;]+);\s*(?P<iter_cmd>[^;]+)\s*\)\s*\{")