
class InvalidDefinition(Exception):
    def __init__(self, key, index, line):
        super().__init__(f"Invalid definition syntax in `{key}`\nat line: {index} => '{line}'")
        
       