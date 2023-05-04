
#include <stdio.h>
#include <cstdlib>
#include <stdint.h>

#include "type_defs.h"
#include "helpers.h"
#include "convertors.h"
#include "instructions.h"
#include "inst_set.h"
#include "bin_loader.h"

#include "memory.h"

k_ptr_t iter;
k_ptr_t mem_sz;
memory *mem;

/*byte_t byte_code[300] = {
    10, 0,
    12, 39, 0, // jump
    // method
    3, 0, // count of args
    4, 0, 5, 0, 6, 0, // args
    18, 23, 0, 4, 0, 5, 0, 6, 0, 
    19,
    // method 2
    3, 0,
    7, 0, 8, 0, 9, 0,
    8, 7, 0, 8, 0, 9, 0,
    19,

    // allocs
    5, 0, 0, 1, 0,
    5, 1, 0, 1, 0,
    5, 2, 0, 1, 0,
    5, 3, 0, 1, 0,
    // sets
    2, 0, 0, 0, 0, 1, 0, 5,
    2, 1, 0, 0, 0, 1, 0, 4,
    2, 3, 0, 0, 0, 1, 0, '\n',
    // code
    18, 5, 0, 2, 0, 0, 0, 1, 0,
    1, 2, 2, 0,
    1, 1, 3, 0,
    0};*/

byte_t pipe(byte_t *byte_code, k_ptr_t iter, memory *mem)
{
    byte_t inst_code = byte_code[iter++];
    while (inst_code < INST_SET_SIZE)
    {
        printf("%u INST[%d]: %d\n", iter, byte_code[iter], inst_code);
        instruction *inst = (instruction *)inst_set[inst_code - 1];
        k_ptr_t ret = inst->run(byte_code, &iter, mem);
        if (!ret) // ret = 0 so this pipe would be ended
            break;
        // instruction CALL return address of its start
        else if (ret > 1)
            if (!pipe(byte_code, ret, mem))
                return 0; // pipe ended with 0 -> exit

        inst_code = byte_code[iter++];
        //mem->prnt_mem();
        //getchar();
    }

    if (inst_code >= INST_SET_SIZE)
    {
        printf("Invalid instruction: %d\n", inst_code);
        return 0;
    }
    if (!inst_code) // KILL
        return 0;
    return 1;
}

int main()
{
    byte_t *byte_code = binloader().getSourceFromFile("test");

    iter = 0;
    mem_sz = getPtr(byte_code, &iter);
    printf("mem size: %d\n", mem_sz);
    mem = new memory(mem_sz);

    pipe(byte_code, iter, mem);

    mem->prnt_mem();
    delete mem;
    delete byte_code;
}