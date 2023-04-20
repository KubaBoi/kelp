
#include <stdio.h>
#include <cstdlib>

#include "type_defs.h"
#include "helpers.h"
#include "convertors.h"
#include "instructions.h"

byte_t mem[100];

int main()
{
    FILE *src_file;
    char ch;
    src_file = fopen("calc.bin", "r");

    int i = 0;
    size_t sz = 100;
    byte_t *source = (byte_t *)malloc(sz);
    
    do {
        if (i >= sz) {
            sz *= 2;
            source = (byte_t *)realloc(source, sz);   
        }
        ch = fgetc(src_file);
        source[i++] = ch;
    } while (ch != EOF);
    fclose(src_file);

    uint_t mem_iter = 0;
    uint_t iter = 0;
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
        // printMem(mem, mem_iter);
    }

    free(source);
}