"""
All precompiled regexes used in compiler
"""

import re

# TODO opravit tenhle regex aby code byl pro vsechny znaky
METHOD_REG = re.compile(r"method\s+(?P<name>[a-zA-Z0-9_]+)\s*\((?P<args_str>[a-zA-Z0-9_,\s]+)\)\s*\{(?P<code>[\s\w\W]*?)\}")

DEC_REG = re.compile(r"^(?P<value>[0-9]+)$")
CHAR_REG = re.compile(r"^'(?P<value>\\[\\'\"0nrtfbv]{1}|.)'$")
STR_REG = re.compile(r"^\"(?P<value>[.\n]*)\"$")

SPLIT_TO_CHARS_REG = re.compile(r"\\[\\'\"0nrtfbv]{1}|.")

ONE_LINE_COM_REG = re.compile(r"//.+\n")

#COMMANDS
RAW_INST_REG = re.compile(r"^\$(?P<inst_name>[a-zA-Z]{2,4})\s+(?P<args>.*)")
ALLOC_REG = re.compile(r"^byte(?P<size>[1-9]*)\s+(?P<var_name>[a-zA-Z0-9_]+)")
SET_DEC_REG = re.compile(r"(?P<var_name>[a-zA-Z0-9_]+)\s*=\s*(?P<value>[0-9]+)$")
SET_CHAR_REG = re.compile(r"(?P<var_name>[a-zA-Z0-9_]+)\s*=\s*'(?P<value>\\[a-z]{1}|.)'$")
SET_STR_REG = re.compile(r"(?P<var_name>[a-zA-Z0-9_]+)\s*=\s*\"(?P<value>[\s\w\W]*)\"$")
SET_BYTES_REG = re.compile(r"(?P<var_name>[a-zA-Z0-9_]+)\s*=\s*\[(?P<value>[\s\w\W]*)\]$")
CALL_REG = re.compile(r"(?P<method>[a-zA-Z0-9_]+)\((?P<args_str>[a-zA-Z0-9_,\s]+)\)")
RTRN_REG = re.compile(r"^return$")