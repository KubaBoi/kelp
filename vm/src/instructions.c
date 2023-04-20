#include "instructions.h"

void out(byte_t *ptr, uint_t *iter, byte_t *mem)
{
    byte_t type = ptr[*iter];
    *iter += 1;
    k_ptr_t addr = getPtr(ptr, iter);
    switch (type)
    {
    case 0: // str
        while (mem[addr] != 0)
            printf("%c", mem[addr++]);
        break;
    case 1: // char
        printf("%c", mem[addr]);
        break;
    case 2: // dec
        printf("%d", mem[addr]);
        break;
    }
}

void set(byte_t *ptr, uint_t *iter, byte_t *mem, uint_t *mem_iter)
{
    byte_t sz = ptr[*iter];
    *iter += 1;
    sz += *iter;
    while (*iter < sz)
    {
        mem[*mem_iter] = ptr[*iter];
        *iter += 1;
        *mem_iter += 1;
    }
}

void sum(byte_t *ptr, uint_t *iter, byte_t *mem)
{
    k_ptr_t addr1 = getPtr(ptr, iter);
    k_ptr_t addr2 = getPtr(ptr, iter);
    k_ptr_t dest = getPtr(ptr, iter);
    mem[dest] = mem[addr1] + mem[addr2];
}

void sub(byte_t *ptr, uint_t *iter, byte_t *mem)
{
    k_ptr_t addr1 = getPtr(ptr, iter);
    k_ptr_t addr2 = getPtr(ptr, iter);
    k_ptr_t dest = getPtr(ptr, iter);
    mem[dest] = mem[addr1] - mem[addr2];
}