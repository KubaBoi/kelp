"""
All precompiled regexes used in compiler
"""

import re

METHOD_FIND_REG = re.compile(r"method\s+[\w\d_]+\s*\([\w\d_,\s]+\)\s*\{")
METHOD_REG = re.compile(r"method\s+(?P<name>[\w\d_]+)\s*\((?P<args_str>[\w\d_,\s]+)\)\s*\{")

DEC_REG = re.compile(r"^(?P<value>[\d]+)$")
CHAR_REG = re.compile(r"^'(?P<value>\\[\\'\"\{\}0nrtfbv]{1}|.)'$")
STR_REG = re.compile(r"^\"(?P<value>[.\n]*)\"$")

SPLIT_TO_CHARS_REG = re.compile(r"\\[\\'\"\{\}0nrtfbv]{1}|.")

ONE_LINE_COM_REG = re.compile(r"//.+\n")
MULTI_LINE_COM_REG = re.compile(r"\/\*[\w\W\s]*?\*\/")

# COMMANDS
RAW_INST_REG = re.compile(r"^\$(?P<inst_name>[\w]{2,4})\s+(?P<args>.*)")
ALLOC_REG = re.compile(r"^byte(?P<size>[1-9]*)\s+(?P<var_name>[\w\d_]+)")
SET_DEC_REG = re.compile(r"(?P<var_name>[\w\d_]+)\s*=\s*(?P<value>[\d]+)$")
SET_CHAR_REG = re.compile(r"(?P<var_name>[\w\d_]+)\s*=\s*'(?P<value>\\[a-z]{1}|.)'$")
SET_STR_REG = re.compile(r"(?P<var_name>[\w\d_]+)\s*=\s*\"(?P<value>[\s\w\W]*)\"$")
SET_BYTES_REG = re.compile(r"(?P<var_name>[\w\d_]+)\s*=\s*\[(?P<value>[\s\w\W]*)\]$")
CPT_REG = re.compile(r"(?P<dest>[\w\d_]+)\s*=\s*(?P<targ>[\w\d_]+)$")
CPY_REG = re.compile(r"(?P<dest>[\w\d_]+)\s*=\s*\*\s*(?P<targ>[\w\d_]+)$")
FOR_CYCLE_REG = re.compile(r"^for\s*\((?P<commands>.*)\)$")
CONTINUE_REG = re.compile(r"^continue$")
BREAK_REG = re.compile(r"^break$")
CALL_REG = re.compile(r"^(?P<method>[\w\d_]+)\((?P<args_str>[\w\d_,\s]+)\)$")
RTRN_REG = re.compile(r"^return$")