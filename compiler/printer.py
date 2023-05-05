"""
Methods for compilation verbose
"""

from config import *

printer_warns = []

def log(*message, end="\n"):
    print(*message, end=end)

def debug(*message, end="\n"):
    if (DEBUG):
        print(*message, end=end)

def error(*message, end="\n"):
    print(f"ERR:", *message, end=end)

def warn(*message, end="\n"):
    printer_warns.append(message)
    print(f"WARN:", *message, end=end)