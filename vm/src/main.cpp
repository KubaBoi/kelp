
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
    byte_t source[300] = {
        4, 0,
        8, 0, 0, 1, 0,
        8, 1, 0, 1, 0,
        8, 2, 0, 1, 0,
        8, 3, 0, 1, 0, // 21
        2, 0, 0, 0, 0, 1, 0, 0,
        2, 1, 0, 0, 0, 1, 0, 10,
        2, 2, 0, 0, 0, 1, 0, 1, // 45
        2, 3, 0, 0, 0, 1, 0, '\n', // 53
        3, 0, 0, 0, 0, 2, 0, // 60
        1, 2, 1, 0, 0,
        1, 1, 0, 3, 0,
        16, 0, 0, 1, 0, 54, 0,
        0};

    iter = 0;
    mem_sz = getPtr(source, &iter);
    mem = new memory(mem_sz);

    uintptr_t insts[16] = {
        (uintptr_t) new OUT(),
        (uintptr_t) new SET(),
        (uintptr_t) new SUM(),
        (uintptr_t) new SUB(),
        (uintptr_t) new MUL(),
        (uintptr_t) new DIV(),
        (uintptr_t) new CPY(),
        (uintptr_t) new ALC(),
        (uintptr_t) new FRE(),
        (uintptr_t) new RLC(),
        (uintptr_t) new JMP(),
        (uintptr_t) new JEQ(),
        (uintptr_t) new JGE(),
        (uintptr_t) new JLE(),
        (uintptr_t) new JG(),
        (uintptr_t) new JL()};

    while (true)
    {
        byte_t inst_code = source[iter++];
        //printf("%u INST[%d]: %d\n", iter, source[iter], inst_code);

        if (!inst_code)
            break;
        instruction *inst = (instruction *)insts[inst_code - 1];
        inst->run(source, &iter, mem);
        //mem->prnt_mem();
        //getchar();
    }
    // mem->prnt_mem();
    delete mem;
    // delete source;
}