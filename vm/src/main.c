
#include <stdio.h>
#include <cstdlib>

#include "type_defs.h"
#include "helpers.h"
#include "convertors.h"
#include "instructions.h"

#include "memory.h"

uint_t iter;
k_ptr_t mem_map_sz;
memory *mem;

byte_t *getSourceFromFile(const char *path)
{
    FILE *src_file;
    char ch;
    src_file = fopen(path, "r");

    size_t i = 0;
    size_t sz = 100;
    byte_t *source = (byte_t *)malloc(sz);

    do
    {
        if (i >= sz)
        {
            sz *= 2;
            source = (byte_t *)realloc(source, sz);
        }
        ch = fgetc(src_file);
        source[i++] = ch;
    } while (ch != EOF);
    fclose(src_file);
    return source;
}

int main()
{
    // byte_t *source = getSourceFromFile("calc.bin");
    /*byte_t source[100] = {
        2, 0,
        8, 0, 0, 3, 0,
        2, 0, 0, 3, 1, 1, 1,
        1, 2, 3, 0, 0,
        0
    };*/
    byte_t source[300] = {
        5, 0,
        8, 0, 0, 1, 0,
        8, 1, 0, 1, 0,
        8, 2, 0, 1, 0,
        8, 3, 0, 9, 0,
        8, 4, 0, 9, 0,
        2, 0, 0, 1, 5,                                          // SET 1 byte as 5
        2, 1, 0, 1, 4,                                          // SET 1 byte as 4
        2, 2, 0, 1, 0,                                          // SET 1 byte as 0
        2, 3, 0, 9, ' ', 'i', 's', ' ', 'm', 'u', 'l', '\n', 0, // SET str into mem
        2, 4, 0, 9, ' ', 'i', 's', ' ', 's', 'u', 'b', '\n', 0, // SET str into mem
        5, 2, 0, 0, 0, 1, 0,                              // SUM value at addres 0 and 1 and fill it into 2
        1, 2, 1, 2, 0,                                    // print addr 2 as dec
        1, 0, 0, 3, 0,                                    // print addr 3 as str
        4, 2, 0, 0, 0, 1, 0,                              // SUB value at addres 0 and 1 and fill it into 2
        1, 2, 1, 2, 0,                                    // print addr 2 as dec
        1, 0, 0, 4, 0,                                   // print addr 3 as str
        0};

    iter = 0;
    mem_map_sz = getPtr(source, &iter);
    mem = new memory(mem_map_sz);

    while (true)
    {
        byte_t inst = source[iter++];
        // printf("%u INST[%d]: %d\n", iter, source[iter], inst);

        if (inst == 0)
            break;
        else if (inst == 1)
            out(source, &iter, mem);
        else if (inst == 2)
            set(source, &iter, mem);
        else if (inst == 3)
            sum(source, &iter, mem);
        else if (inst == 4)
            sub(source, &iter, mem);
        else if (inst == 5)
            mul(source, &iter, mem);
        else if (inst == 6)
            div(source, &iter, mem);
        else if (inst == 7)
            cpy(source, &iter, mem);
        else if (inst == 8)
            alc(source, &iter, mem);
        else
        {
            printf("Invalid instruction '%d' at position: %d\n", inst, iter);
            printf("Terminating\n");
            break;
        }
        //printMem(mem, mem_iter);
        // getchar();
    }
    delete mem;
    // free(source);
}