#include "instructions.h"

void out(byte_t *ptr, uint_t *iter, byte_t *mem)
{
    byte_t type = ptr[*iter];
    k_ptr_t addr;
    *iter += 1;
    switch (type)
    {
    case 0: // str
        addr = getPtr(ptr, iter);
        while (mem[addr] != 0)
            printf("%c", mem[addr++]);
        break;
    case 1: // char
        addr = getPtr(ptr, iter);
        printf("%c", mem[addr]);
        break;
    case 2: // dec
        byte_t byte_count = ptr[*iter];
        *iter += 1;
        addr = getPtr(ptr, iter);
        printf("%d", toInt(&mem[addr], byte_count));
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
    k_ptr_t dest = getPtr(ptr, iter);
    k_ptr_t addr1 = getPtr(ptr, iter);
    k_ptr_t addr2 = getPtr(ptr, iter);
    mem[dest] = mem[addr1] + mem[addr2];
}

void sub(byte_t *ptr, uint_t *iter, byte_t *mem)
{
    k_ptr_t dest = getPtr(ptr, iter);
    k_ptr_t addr1 = getPtr(ptr, iter);
    k_ptr_t addr2 = getPtr(ptr, iter);
    mem[dest] = mem[addr1] - mem[addr2];
}

void cpy(byte_t *ptr, uint_t *iter, byte_t *mem)
{
    byte_t sz = ptr[*iter];
    *iter += 1;
    k_ptr_t dest = getPtr(ptr, iter);
    k_ptr_t addr = getPtr(ptr, iter);
    for (byte_t i = 0; i < sz; i++)
        mem[dest + i] = mem[addr + i];
}