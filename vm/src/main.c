
#include <stdio.h>
#include <cstdlib>

#include "type_defs.h"
#include "helpers.h"
#include "convertors.h"
#include "instructions.h"

byte_t source[100] = {
    0, 0, 0, 63,                                      // first 4 bytes are size of array
    2, 1, 5,                                          // SET 1 byte as 5
    2, 1, 4,                                          // SET 1 byte as 4
    2, 1, 0,                                          // SET 1 byte as 0
    2, 9, ' ', 'i', 's', ' ', 's', 'u', 'm', '\n', 0, // SET str into mem
    2, 9, ' ', 'i', 's', ' ', 's', 'u', 'b', '\n', 0, // SET str into mem
    3, 0, 0, 0, 1, 0, 2,                              // SUM value at addres 0 and 1 and fill it into 2
    1, 2, 0, 2,                                       // print addr 2 as dec
    1, 0, 0, 3,                                       // print addr 3 as str
    4, 0, 0, 0, 1, 0, 2,                              // SUB value at addres 0 and 1 and fill it into 2
    1, 2, 0, 2,                                       // print addr 2 as dec
    1, 0, 0, 12,                                      // print addr 3 as str
};

byte_t mem[100];

int main()
{
    uint_t size = toInt(source);

    uint_t mem_iter = 0;
    uint_t iter = 4;
    while (iter < size)
    {
        byte_t inst = source[iter++];
        // printf("%u INST[%d]: %d\n", iter, source[iter], inst);

        if (inst == 1)
            out(source, &iter, mem);
        else if (inst == 2)
            set(source, &iter, mem, &mem_iter);
        else if (inst == 3)
            sum(source, &iter, mem);
        else if (inst == 4)
            sub(source, &iter, mem);
        // printMem(mem, mem_iter);
    }
}