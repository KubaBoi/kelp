
from vars import *

class instruction:
    def __init__(self, content: str, index: int):
        self.content = content
        self.index = index

class object:
    def __init__(self, name = "root", type = "file", level = -1, index = 0, parent = None) -> None:
        self.name = name
        self.type = type
        self.level = level
        self.index = index
        self.parent = parent
        self.objects = {}
        self.instructions = []
        
    def add_object(self, obj: object):
        self.objects[obj.name] = obj
        
    def print(self):
        print(f"{self.index}: {' '*self.level}{self.name}: {self.type} - {self.level}")
        for inst in self.instructions:
            print(f"{inst.index}: {' '*(self.level + 4)}{inst.content}")
        print()
        for key in self.objects.keys():
            obj = self.objects[key]
            obj.print()

class kelp_comp:
    
    # source data lines
    src_dtl = ""
    
    keywords = [
        "class",
        "def"
    ]
    
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
        
        parent = root
        while (index < length):
            line = kelp_comp.src_dtl[index].rstrip()
            lline = line.lstrip()
            index += 1
            level = len(line) - len(lline)
            if (level % 4 != 0):
                print(f"Invalid spaces at line: {index}")
                return 0
            if (len(lline) < 1):
                continue
            if (lline == "from kelp import *"):
                continue
            
            tp, name = kelp_comp.get_type_name(lline, parent.name, index)
            if (name == None):
                parent.instructions.append(instruction(tp, index))
                continue
                
            if (level < parent.level):
                obj = object(name, tp, level, index, parent)
                parent.add_object(obj)
            elif (level == parent.level):
                parent = parent.parent
                obj = object(name, tp, level, index, parent)
                parent.add_object(obj)
                parent = obj
            else:
                while (level >= parent.level and parent.level >= 0):
                    parent = parent.parent
                obj = object(name, tp, level, index, parent)
                parent.add_object(obj)
                parent = obj
        root.print()
        
        
            
    @staticmethod
    def get_type_name(line: str, key: str, index: int) -> list[2]:
        # Return type and name of class/def from line
        splt = line.split(" ")
        if (splt[0] not in kelp_comp.keywords):
            return (line, None)
        if (len(splt) < 2):
            raise InvalidDefinition(key, index, line)
        splt[1] = " ".join(splt[1:])
        splt[1] = splt[1].split(":")[0]
        return tuple(splt[:2])
        
if __name__ == "__main__":
    kelp_comp.load("testApp.py")
    kelp_comp.compile()