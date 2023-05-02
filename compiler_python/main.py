data_calc = [
    7, 0,
    12, 21, 0, # jump
    # method
    3, 0, # count of args
    4, 0, 5, 0, 6, 0, # args
    8, 4, 0, 5, 0, 6, 0, # sum 5 0 + 6 0 -> 4 0
    19,
    # allocs
    5, 0, 0, 1, 0,
    5, 1, 0, 1, 0,
    5, 2, 0, 1, 0,
    5, 3, 0, 1, 0,
    # sets
    2, 0, 0, 0, 0, 1, 0, 5,
    2, 1, 0, 0, 0, 1, 0, 4,
    2, 3, 0, 0, 0, 1, 0, '\n',
    # code
    18, 5, 0, 2, 0, 0, 0, 1, 0,
    1, 2, 2, 0,
    1, 1, 3, 0,
    0
]

with open("calc.bin", "wb") as f:
    for c in data_calc:
        if (isinstance(c, str)):
            c = ord(c)
        f.write(c.to_bytes())        