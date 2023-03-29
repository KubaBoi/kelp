
from vars import *

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
    
    @staticmethod
    def load(path: str):
        with open(path, "r", encoding="utf-8") as f:
            kelp_comp.src_dtl = f.readlines()
            
    @staticmethod
    def compile():
        # Start compilation
        index = 0
        length = len(kelp_comp.src_dtl)
        while (index < length):
            line = kelp_comp.src_dtl[index]
            index += 1
            if (line.startswith("class")):
                name = kelp_comp.get_cls_name(line)
                kelp_comp.classes[name] = []
                line = kelp_comp.src_dtl[index]
                # create class data bundle [0] - name, [1] - instructions of class
                while (not line.startswith("class")):
                    stripped = line.strip()
                    if (len(stripped) > 0 and stripped != "pass"):
                        kelp_comp.classes[name].append((index + 1, stripped))
                    index += 1
                    if (index >= length):
                        break
                    line = kelp_comp.src_dtl[index]
        
        try:
            kelp_comp.config_vars = vars.prepare_vars(kelp_comp.classes, "config")
            kelp_comp.global_vars = vars.prepare_vars(kelp_comp.classes, "vars")
            kelp_comp.lv_objs = vars.prepare_vars(kelp_comp.classes, "lv_objs")
        except InvalidDefinition as e:
            print(e)
            return 0
        
            
    @staticmethod
    def get_cls_name(line: str):
        # Return name of class from line
        return line.replace("class ", "").replace(":", "").strip()
        
if __name__ == "__main__":
    kelp_comp.load("testApp.py")
    kelp_comp.compile()