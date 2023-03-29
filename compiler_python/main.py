
from vars import *

class object:
    def __init__(self, name = "root", type = "file", index = -1, parent = None) -> None:
        self.name = name
        self.type = type
        self.index = index
        self.parent = parent

class kelp_comp:
    
    # source data lines
    src_dtl = ""
    # dict of classes
    classes = {}
    # dicts of variables
    config_vars = {}
    global_vars = {}
    lv_objs = {}
    # dicts of functions
    funcs = {}
    ints = {}
    
    root = None
    
    @staticmethod
    def load(path: str):
        with open(path, "r", encoding="utf-8") as f:
            kelp_comp.src_dtl = f.readlines()
            
    @staticmethod
    def compile():
        # Start compilation
        root = object()
        index = 0
        length = len(kelp_comp.src_dtl)
        while (index < length):
            line = kelp_comp.src_dtl[index].rstrip()
            lline = line.lstrip()
            index += 1
            level = len(line) - len(lline)
            if (level % 4 != 0):
                print(f"Invalid spaces at line: {index}")
                return 0
        
            
    @staticmethod
    def get_type_name(line: str, key: str, index: int) -> list[2]:
        # Return type and name of class/def from line
        splt = line.split(" ")
        if (len(splt) < 2):
            raise InvalidDefinition(key, index, line)
        splt[1] = " ".join(splt[1:])
        splt[1] = splt[1].split(":")[0]
        return splt
        
if __name__ == "__main__":
    kelp_comp.load("testApp.py")
    kelp_comp.compile()