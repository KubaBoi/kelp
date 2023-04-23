
#include <stdio.h>
#include <cstdlib>

#include "type_defs.h"
#include "helpers.h"
#include "convertors.h"
#include "instructions.h"

#include "memory.h"

byte_t mem[100];
uint_t mem_iter;
uint_t iter;
k_ptr_t mem_map_sz;
k_ptr_t *mem_map;

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
        2, 3, 1, 1, 1,
        1, 2, 3, 0, 0,
        0
    };*/
    byte_t source[100] = {
        5, 0,
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
        1, 0, 0, 3, 0,                                   // print addr 3 as str
        7, 1, 2, 0, 0, 0,
        0};

    mem_iter = 1;
    iter = 0;
    mem_map_sz = getPtr(source, &iter);
    mem_map = (k_ptr_t *)malloc(sizeof(mem_map) * mem_map_sz);
    for (k_ptr_t i = 0; i < mem_map_sz; i++)
        mem_map[i] = 0;

    while (true)
    {
        byte_t inst = source[iter++];
        // printf("%u INST[%d]: %d\n", iter, source[iter], inst);

        if (inst == 0)
            break;
        else if (inst == 1)
            out(source, &iter, mem);
        else if (inst == 2)
            set(source, &iter, mem, &mem_iter);
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
        else
        {
            printf("Invalid instruction '%d' at position: %d\n", inst, iter);
            printf("Terminating\n");
            break;
        }
        //printMem(mem, mem_iter);
        // getchar();
    }
    free(mem_map);
    // free(source);
}