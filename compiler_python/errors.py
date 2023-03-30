
class InvalidDefinition(Exception):
    def __init__(self, key, index, line):
        super().__init__(f"Invalid definition syntax in `{key}`\nat line: {index} => '{line}'")
        
class InvalidSpaces(Exception):
    def __init__(self, key, index, line):
        super().__init__(f"Invalid spaces in `{key}`\nat line: {index} => '{line}'")
        
class InvalidImport(Exception):
    def __init__(self, file, index, line):
        super().__init__(f"Invalid import in `{file}`\nat line: {index} => '{line}'")
        
class ImportNotFound(Exception):
    def __init__(self, imp, file, index, line):
        super().__init__(f"Import '{imp}' was not found in '{file}'\nat line: {index} => '{line}'")