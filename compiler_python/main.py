
import os
import re

from errors import *
from objects import *

class kelp_comp:
    
    keywords = [
        "class",
        "def"
    ]
    
    prog = re.compile("from ([a-zA-Z0-9\.\_]+) import ([a-zA-Z0-9\_\*]+)")
        
    @staticmethod
    def load(path: str):
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
            
    @staticmethod
    def imports(file: str, lines: list):
        """
        Method recursively import file

        Args:
            `file`: file path
            `lines`: lines of the file

        Raises:
            InvalidImport: Import syntax is odd
            ImportNotFound: Import file was not found

        Returns:
            list: list of lines with imports
        """
        for i, line in enumerate(lines):
            res = re.search(kelp_comp.prog, line)
            if (res == None):
                continue
            
            if (len(res.groups()) != 2):
                raise InvalidImport(file, i, line)
            
            fl = res.group(1).split(".")
            keys = res.group(2).split(".")
            imp = os.path.join(os.path.dirname(file), *fl) + ".py"
            if (not os.path.exists(imp)):
                raise ImportNotFound(imp, file, i, line)
            
            tree = kelp_comp.build_tree(imp)
            tree = tree.get_object(*keys)
            if (tree == None):
                raise ImportNotFound(".".join(keys), file, i, line)
            lines[i] = tree.to_string()        
            
        return "\n".join(lines).split("\n")
            
            
    @staticmethod
    def build_tree(path: str):
        src_dtl = kelp_comp.load(path)
        src_dtl = kelp_comp.imports(path, src_dtl)
        root = object(name=path)
        index = 0
        length = len(src_dtl)
        
        parent = root
        while (index < length):
            line = src_dtl[index].rstrip()
            lline = line.lstrip()
            if (len(lline) < 1):
                index += 1
                continue
            index += 1
            level = len(line) - len(lline)
            if (level % 4 != 0):
                raise InvalidSpaces(parent.name, index, lline)
            if (lline.startswith("\"\"\"")):
                index += 1
                while (index < length):
                    line = src_dtl[index].rstrip()
                    index += 1
                    if (line.endswith("\"\"\"")):
                        break
                index += 1    
                continue
                    
            
            tp, name = kelp_comp.get_type_name(lline, parent.name, index)
            if (name == None):
                parent.instructions.append(instruction(tp, index))
                continue
                
            if (level < parent.level):
                obj = object(name.split("(")[0], name, tp, level, index, parent)
                parent.add_object(obj)
            elif (level == parent.level):
                parent = parent.parent
                obj = object(name.split("(")[0], name, tp, level, index, parent)
                parent.add_object(obj)
                parent = obj
            else:
                while (level >= parent.level and parent.level >= 0):
                    parent = parent.parent
                obj = object(name.split("(")[0], name, tp, level, index, parent)
                parent.add_object(obj)
                parent = obj
        return root
            
    @staticmethod
    def compile(path: str):
        # Start compilation
        root = kelp_comp.build_tree(path)
        root.print()
        with open("temp.py", "w", encoding="utf-8") as f:
            f.write(root.to_string())
        
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
    #try:
    kelp_comp.compile("testApp.py")
    #except Exception as e:
    #    print(e)