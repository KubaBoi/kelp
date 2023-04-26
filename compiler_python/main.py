data_calc = [
    5, 0,
    8, 0, 0, 1, 0,
    8, 1, 0, 1, 0,
    8, 2, 0, 1, 0,
    8, 3, 0, 9, 0,
    8, 4, 0, 9, 0,
    2, 0, 0, 0, 0, 1, 0, 5,                                          
    2, 1, 0, 0, 0, 1, 0, 4,                                          
    2, 2, 0, 0, 0, 1, 0, 0,                                          
    2, 3, 0, 0, 0, 9, 0, ' ', 'i', 's', ' ', 'm', 'u', 'l', '\n', 0, 
    2, 4, 0, 0, 0, 9, 0, ' ', 'i', 's', ' ', 's', 'u', 'b', '\n', 0, 
    5, 2, 0, 0, 0, 1, 0,                                    
    1, 2, 1, 2, 0,                                          
    1, 0, 0, 3, 0,                                          
    4, 2, 0, 0, 0, 1, 0,                                    
    1, 2, 1, 2, 0,                                          
    1, 0, 0, 4, 0,                                          
    0                  
]      

with open("calc.bin", "wb") as f:
    for c in data_calc:
        if (isinstance(c, str)):
            c = ord(c)
        f.write(c.to_bytes())        