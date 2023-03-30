
class instruction:
    def __init__(self, content: str, index: int):
        self.content = content
        self.index = index

class object:
    def __init__(self, name = "global", real_name="", type = "file", level = -1, index = 0, parent = None) -> None:
        self.name = name
        self.real_name = real_name
        self.type = type
        self.level = level
        self.index = index
        self.parent = parent
        self.objects = {}
        self.instructions = []
        
    def add_object(self, obj: object):
        self.objects[obj.name] = obj
        
    def get_object(self, *args):
        tree = self
        if (len(args) == 1 and args[0] == "*"):
            return tree
        for key in args:
            if (key not in tree.objects.keys()):
                return None
            tree = tree.objects[key]
        return tree
        
    def print(self):
        print(f"{self.index}: {' '*self.level}{self.real_name}: {self.type} - {self.level} - OBJ")
        for inst in self.instructions:
            print(f"{inst.index}: {' '*(self.level + 4)}{inst.content} - INS")
        print()
        for key in self.objects.keys():
            obj = self.objects[key]
            obj.print()
            
    def to_string(self, s=""):
        multip = 0
        if (self.level != -1):
            multip = 4
            s += f"{' '*(self.level)}{self.type} {self.real_name}:\n"
        
        for inst in self.instructions:
            s += f"{' '*(self.level + multip)}{inst.content}\n"
        for key in self.objects.keys():
            obj = self.objects[key]
            s = obj.to_string(s)
        return s
        
