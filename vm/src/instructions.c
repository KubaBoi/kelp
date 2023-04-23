#include "instructions.h"

void out(byte_t *ptr, uint_t *iter, memory *mem)
{
    byte_t type = getNextByte(ptr, iter);
    byte_t byte_count = getNextByte(ptr, iter);
    k_ptr_t addr = getPtr(ptr, iter);
    switch (type)
    {
    case 0: // str
    {
        byte_t offset = 0;
        while (mem->get_byte(addr, offset) != 0)
            printf("%c", mem->get_byte(addr, offset++));
        break;
    }
    case 1: // char
    {
        printf("%c", mem->get_byte(addr));
        break;
    }
    case 2: // dec
    {
        printf("%lld", mem->get_dec(addr, byte_count));
        break;
    }
    case 3: // list of char
    {
        for (byte_t i = 0; i < byte_count; i++)
            printf("%c", mem->get_byte(addr, i));
        break;
    }
    }
}

void set(byte_t *ptr, uint_t *iter, memory *mem)
{
    k_ptr_t addr = getPtr(ptr, iter);
    byte_t sz = ptr[*iter];
    *iter += 1;
    sz += *iter;
    byte_t i = 0;
    while (*iter < sz)
    {
        mem->set_byte(addr, ptr[*iter], i++);
        *iter += 1;
    }
}

void sum(byte_t *ptr, uint_t *iter, memory *mem)
{
    k_ptr_t dest = getPtr(ptr, iter);
    k_ptr_t addr1 = getPtr(ptr, iter);
    k_ptr_t addr2 = getPtr(ptr, iter);
    byte_t res = mem->get_byte(addr1) + mem->get_byte(addr2);
    mem->set_byte(dest, res);
}

void sub(byte_t *ptr, uint_t *iter, memory *mem)
{
    k_ptr_t dest = getPtr(ptr, iter);
    k_ptr_t addr1 = getPtr(ptr, iter);
    k_ptr_t addr2 = getPtr(ptr, iter);
    byte_t res = mem->get_byte(addr1) - mem->get_byte(addr2);
    mem->set_byte(dest, res);
}

void mul(byte_t *ptr, uint_t *iter, memory *mem)
{
    k_ptr_t dest = getPtr(ptr, iter);
    k_ptr_t addr1 = getPtr(ptr, iter);
    k_ptr_t addr2 = getPtr(ptr, iter);
    byte_t res = mem->get_byte(addr1) * mem->get_byte(addr2);
    mem->set_byte(dest, res);
}

void div(byte_t *ptr, uint_t *iter, memory *mem)
{
    k_ptr_t dest = getPtr(ptr, iter);
    k_ptr_t mod = getPtr(ptr, iter);
    k_ptr_t addr1 = getPtr(ptr, iter);
    k_ptr_t addr2 = getPtr(ptr, iter);
    byte_t res = mem->get_byte(addr1) / mem->get_byte(addr2);
    byte_t md = mem->get_byte(addr1) - (res * mem->get_byte(addr2));
    mem->set_byte(dest, res);
    mem->set_byte(mod, md);
}

void cpy(byte_t *ptr, uint_t *iter, memory *mem)
{
    byte_t sz = ptr[*iter];
    *iter += 1;
    k_ptr_t dest = getPtr(ptr, iter);
    k_ptr_t addr = getPtr(ptr, iter);
    for (byte_t i = 0; i < sz; i++)
    {
        byte_t bt = mem->get_byte(addr, i);
        mem->set_byte(dest, bt, i);
    }
}