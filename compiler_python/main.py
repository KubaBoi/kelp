data_calc = [
    2, 1, 5,                                          # SET 1 byte as 5
    2, 1, 4,                                          # SET 1 byte as 4
    2, 1, 0,                                          # SET 1 byte as 0
    2, 9, ' ', 'i', 's', ' ', 's', 'u', 'm', '\n', 0, # SET str into mem
    2, 9, ' ', 'i', 's', ' ', 's', 'u', 'b', '\n', 0, # SET str into mem
    3, 2, 0, 0, 0, 1, 0,                              # SUM value at addres 0 and 1 and fill it into 2
    1, 2, 2, 0,                                       # print addr 2 as dec
    1, 0, 3, 0,                                       # print addr 3 as str
    4, 2, 0, 0, 0, 1, 0,                              # SUB value at addres 0 and 1 and fill it into 2
    1, 2, 2, 0,                                       # print addr 2 as dec
    1, 0, 12, 0,                                      # print addr 3 as str
    0                                                 # end
]      

data_copy = [
    2, 1, 6,                
    2, 1, 8,
    2, 1, 0,
    5, 1, 1, 0, 0, 0,       # CPY 0 -> 1
    3, 2, 0, 0, 0, 1, 0,    # SUM 0 + 1 -> 2
    1, 2, 1, 2, 0,          # print 2
    0 
]

with open("calc.bin", "wb") as f:
    for c in data_calc:
        if (isinstance(c, str)):
            c = ord(c)
        f.write(c.to_bytes())        