#include "instructions.h"

void instruction::run(byte_t *ptr, uint_t *iter, memory *mem){};

void OUT::run(byte_t *ptr, uint_t *iter, memory *mem)
{
    byte_t type = getNextByte(ptr, iter);
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
        printf("%lld", mem->get_dec(addr, mem->get_size(addr)));
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
    uint128_t val1 = mem->get_dec(addr1, mem->get_size(addr1));
    uint128_t val2 = mem->get_dec(addr2, mem->get_size(addr2));
    uint128_t res = val1 + val2;
    word_t sz;
    byte_t *bt_arr = mem->get_bytes(dest, &sz);
    toCharArray(sz, res, bt_arr);
}

void SUB::run(byte_t *ptr, uint_t *iter, memory *mem)
{
    k_ptr_t dest = getPtr(ptr, iter);
    k_ptr_t addr1 = getPtr(ptr, iter);
    k_ptr_t addr2 = getPtr(ptr, iter);
    uint128_t val1 = mem->get_dec(addr1, mem->get_size(addr1));
    uint128_t val2 = mem->get_dec(addr2, mem->get_size(addr2));
    uint128_t res = val1 - val2;
    word_t sz;
    byte_t *bt_arr = mem->get_bytes(dest, &sz);
    toCharArray(sz, res, bt_arr);
}

void MUL::run(byte_t *ptr, uint_t *iter, memory *mem)
{
    k_ptr_t dest = getPtr(ptr, iter);
    k_ptr_t addr1 = getPtr(ptr, iter);
    k_ptr_t addr2 = getPtr(ptr, iter);
    uint128_t val1 = mem->get_dec(addr1, mem->get_size(addr1));
    uint128_t val2 = mem->get_dec(addr2, mem->get_size(addr2));
    uint128_t res = val1 * val2;
    word_t sz;
    byte_t *bt_arr = mem->get_bytes(dest, &sz);
    toCharArray(sz, res, bt_arr);
}

void DIV::run(byte_t *ptr, uint_t *iter, memory *mem)
{
    k_ptr_t dest = getPtr(ptr, iter);
    k_ptr_t mod = getPtr(ptr, iter);
    k_ptr_t addr1 = getPtr(ptr, iter);
    k_ptr_t addr2 = getPtr(ptr, iter);
    uint128_t val1 = mem->get_dec(addr1, mem->get_size(addr1));
    uint128_t val2 = mem->get_dec(addr2, mem->get_size(addr2));
    uint128_t res = val1 / val2;
    uint128_t mod_res = val1 - (res * val2);
    word_t sz;
    byte_t *bt_arr = mem->get_bytes(dest, &sz);
    toCharArray(sz, res, bt_arr);
    bt_arr = mem->get_bytes(mod, &sz);
    toCharArray(sz, mod_res, bt_arr);
}

void CPY::run(byte_t *ptr, uint_t *iter, memory *mem)
{
    byte_t sz = getNextByte(ptr, iter);
    k_ptr_t dest = getPtr(ptr, iter);
    k_ptr_t addr = getPtr(ptr, iter);
    for (byte_t i = 0; i < sz; i++)
        mem->set_byte(dest, mem->get_byte(addr, i), i);
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

void JMP::run(byte_t *ptr, uint_t *iter, memory *mem)
{
    k_ptr_t addr = getPtr(ptr, iter);
    *iter = addr;
}

void JEQ::run(byte_t *ptr, uint_t *iter, memory *mem)
{
    k_ptr_t arg0 = getPtr(ptr, iter);
    k_ptr_t arg1 = getPtr(ptr, iter);
    k_ptr_t addr = getPtr(ptr, iter);
    uint128_t v0 = mem->get_dec(arg0, mem->get_size(arg0));
    uint128_t v1 = mem->get_dec(arg1, mem->get_size(arg1));
    if (v0 == v1)
        *iter = addr;
}

void JGE::run(byte_t *ptr, uint_t *iter, memory *mem)
{
    k_ptr_t arg0 = getPtr(ptr, iter);
    k_ptr_t arg1 = getPtr(ptr, iter);
    k_ptr_t addr = getPtr(ptr, iter);
    uint128_t v0 = mem->get_dec(arg0, mem->get_size(arg0));
    uint128_t v1 = mem->get_dec(arg1, mem->get_size(arg1));
    if (v0 >= v1)
        *iter = addr;
}

void JLE::run(byte_t *ptr, uint_t *iter, memory *mem)
{
    k_ptr_t arg0 = getPtr(ptr, iter);
    k_ptr_t arg1 = getPtr(ptr, iter);
    k_ptr_t addr = getPtr(ptr, iter);
    uint128_t v0 = mem->get_dec(arg0, mem->get_size(arg0));
    uint128_t v1 = mem->get_dec(arg1, mem->get_size(arg1));
    if (v0 <= v1)
        *iter = addr;
}

void JG::run(byte_t *ptr, uint_t *iter, memory *mem)
{
    k_ptr_t arg0 = getPtr(ptr, iter);
    k_ptr_t arg1 = getPtr(ptr, iter);
    k_ptr_t addr = getPtr(ptr, iter);
    uint128_t v0 = mem->get_dec(arg0, mem->get_size(arg0));
    uint128_t v1 = mem->get_dec(arg1, mem->get_size(arg1));
    if (v0 > v1)
        *iter = addr;
}

void JL::run(byte_t *ptr, uint_t *iter, memory *mem)
{
    k_ptr_t arg0 = getPtr(ptr, iter);
    k_ptr_t arg1 = getPtr(ptr, iter);
    k_ptr_t addr = getPtr(ptr, iter);
    uint128_t v0 = mem->get_dec(arg0, mem->get_size(arg0));
    uint128_t v1 = mem->get_dec(arg1, mem->get_size(arg1));
    if (v0 < v1)
        *iter = addr;
}