
BASE = 256

def from_256(arr: list) -> int:
    res = arr[0]
    for i, a in enumerate(arr):
        res += a * (BASE * i)
    return res

def to_256(value: int, byte_size = None) -> list:
    """
    Convert integer into 256-decimal system as little endian
    and fill zeros if needed to wanted `byte_size`

    if `byte_size` is None than return list without filling
    """
    arr = []
    val_v = value
    while val_v >= BASE:
        arr.append(val_v // BASE)
        val_v = val_v % BASE
    arr.append(val_v)
    arr.reverse()
    if (byte_size == None):
        return arr
    
    ln = len(arr)
    if (ln > byte_size):
        raise OverflowError(f"Decimal {value} cannot be converted to {byte_size}bytes")
    elif (ln < byte_size):
        for i in range(ln, byte_size):
            arr.append(0)
    return arr

