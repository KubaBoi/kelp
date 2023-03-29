
from errors import *

class variable:
    def __init__(self, name, value, index) -> None:
        self.name = name
        self.value = value
        self.index = index

class vars:
    
    @staticmethod
    def prepare_vars(data_classes: list, key: str) -> dict:
        """
        Prepare list of global variables or config

        Args:
            `data` : dict of tuples "key": [(line index, line content),...]
            `return`: dict of variables and their values
        """
        variables = {}
        if (key in data_classes.keys()):
            for line in data_classes[key]:
                splt = line[1].split("#")[0].split("=")
                if (len(splt) != 2):
                    raise InvalidDefinition(line[0], line[1])
                name = splt[0].strip()
                variables[name] = variable(name, splt[1].strip(), line[0])

        if (key == "config"):
            if ("mode" not in variables.keys()):
                variables["mode"] = variable("mode", "MODE_SHL", 0)
            if ("name" not in variables.keys()):
                variables["name"] = variable("name", "Chilli Boi", 0)
        return variables
            
        