
ESCAPE_CHARS = {
    "\\": ord("\\"),
    "\'": ord("'"),
    "\"": ord("\""),
    "n": ord("\n"),
    "r": ord("\r"),
    "t": ord("\t"),
    "b": ord("\b"),
    "f": ord("\f"),
    "v": ord("\v"),
    "0": ord("\0")
}

def get_ord(char: str) -> int:
    """
    Return byte of character
    """
    if (len(char) == 1):
        return ord(char)
    if (char[1] not in ESCAPE_CHARS.keys()):
        raise SyntaxError(f"Escape character {char} does not exists or is not allowed")
    return ESCAPE_CHARS[char[1]]