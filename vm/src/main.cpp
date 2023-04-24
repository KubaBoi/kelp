
#include <stdio.h>
#include <cstdlib>
#include <stdint.h>

#include "type_defs.h"
#include "helpers.h"
#include "convertors.h"
#include "instructions.h"

#include "memory.h"

uint_t iter;
k_ptr_t mem_sz;
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
        5, 2, 0, 0, 0, 1, 0,                                    // SUM value at addres 0 and 1 and fill it into 2
        1, 2, 1, 2, 0,                                          // print addr 2 as dec
        1, 0, 0, 3, 0,                                          // print addr 3 as str
        4, 2, 0, 0, 0, 1, 0,                                    // SUB value at addres 0 and 1 and fill it into 2
        1, 2, 1, 2, 0,                                          // print addr 2 as dec
        1, 0, 0, 4, 0,                                          // print addr 3 as str
        0};

    iter = 0;
    mem_sz = getPtr(source, &iter);
    mem = new memory(mem_sz);

    uintptr_t insts[10] = {
        (uintptr_t)new OUT(),
        (uintptr_t)new SET(),
        (uintptr_t)new SUM(),
        (uintptr_t)new SUB(),
        (uintptr_t)new MUL(),
        (uintptr_t)new DIV(),
        (uintptr_t)new CPY(),
        (uintptr_t)new ALC(),
        (uintptr_t)new FRE(),
        (uintptr_t)new RLC()
    };

    while (true)
    {
        byte_t inst_code = source[iter++];
        //printf("%u INST[%d]: %d\n", iter, source[iter], inst_code);

        if (!inst_code)
            break;
        instruction *inst = (instruction *)insts[inst_code - 1];
        inst->run(source, &iter, mem);
        // printMem(mem, mem_iter);
        // getchar();
    }
    mem->prnt_mem();
    delete mem;
    //delete source;
}