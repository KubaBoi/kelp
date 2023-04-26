#include "instructions.h"

void instruction::run(byte_t *ptr, uint_t *iter, memory *mem){};

void OUT::run(byte_t *ptr, uint_t *iter, memory *mem)
{
    byte_t type = getNextByte(ptr, iter);
    byte_t byte_count = getNextByte(ptr, iter);
    k_ptr_t addr = getPtr(ptr, iter);
    switch (type)
    {
    case 0: // str
        printf("%s", mem->get_mem(addr));
        break;
    case 1: // char
        printf("%c", mem->get_byte(addr));
        break;
    case 2: // dec
        printf("%lld", mem->get_dec(addr, byte_count));
        break;
    case 3: // list of char
        printf("%.*s", byte_count, mem->get_mem(addr));
        break;
    }
}

void SET::run(byte_t *ptr, uint_t *iter, memory *mem)
{
    k_ptr_t addr = getPtr(ptr, iter);
    word_t offset = getPtr(ptr, iter);
    word_t sz = getPtr(ptr, iter);
    sz += *iter;
    while (*iter < sz)
    {
        mem->set_byte(addr, ptr[*iter], offset++);
        *iter += 1;
    }
}

void SUM::run(byte_t *ptr, uint_t *iter, memory *mem)
{
    k_ptr_t dest = getPtr(ptr, iter);
    k_ptr_t addr1 = getPtr(ptr, iter);
    k_ptr_t addr2 = getPtr(ptr, iter);
    byte_t res = mem->get_byte(addr1) + mem->get_byte(addr2);
    mem->set_byte(dest, res);
}

void SUB::run(byte_t *ptr, uint_t *iter, memory *mem)
{
    k_ptr_t dest = getPtr(ptr, iter);
    k_ptr_t addr1 = getPtr(ptr, iter);
    k_ptr_t addr2 = getPtr(ptr, iter);
    byte_t res = mem->get_byte(addr1) - mem->get_byte(addr2);
    mem->set_byte(dest, res);
}

void MUL::run(byte_t *ptr, uint_t *iter, memory *mem)
{
    k_ptr_t dest = getPtr(ptr, iter);
    k_ptr_t addr1 = getPtr(ptr, iter);
    k_ptr_t addr2 = getPtr(ptr, iter);
    byte_t res = mem->get_byte(addr1) * mem->get_byte(addr2);
    mem->set_byte(dest, res);
}

void DIV::run(byte_t *ptr, uint_t *iter, memory *mem)
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

void CPY::run(byte_t *ptr, uint_t *iter, memory *mem)
{
    byte_t sz = getNextByte(ptr, iter);
    k_ptr_t dest = getPtr(ptr, iter);
    k_ptr_t addr = getPtr(ptr, iter);
    for (byte_t i = 0; i < sz; i++)
    {
        byte_t bt = mem->get_byte(addr, i);
        mem->set_byte(dest, bt, i);
    }
}

void ALC::run(byte_t *ptr, uint_t *iter, memory *mem)
{
    k_ptr_t addr = getPtr(ptr, iter);
    word_t byte_count = getPtr(ptr, iter);
    mem->alloc(addr, byte_count);
}

void FRE::run(byte_t *ptr, uint_t *iter, memory *mem)
{
    k_ptr_t addr = getPtr(ptr, iter);
    mem->free_mem(addr);
}

void RLC::run(byte_t *ptr, uint_t *iter, memory *mem)
{
    k_ptr_t addr = getPtr(ptr, iter);
    word_t byte_count = getPtr(ptr, iter);
    mem->reallc(addr, byte_count);
}

void MB::run(byte_t *ptr, uint_t *iter, memory *mem)
{
    word_t bytes = getPtr(ptr, iter);
    *iter -= bytes;
}

void FB::run(byte_t *ptr, uint_t *iter, memory *mem)
{
    word_t bytes = getPtr(ptr, iter);
    *iter += bytes;
}

void JMP::run(byte_t *ptr, uint_t *iter, memory *mem)
{
    k_ptr_t addr = getPtr(ptr, iter);
}