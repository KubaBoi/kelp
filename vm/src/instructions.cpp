#include "instructions.h"

k_ptr_t instruction::run(byte_t *ptr, k_ptr_t *iter, memory *mem) { return 1; };

k_ptr_t OUT::run(byte_t *ptr, k_ptr_t *iter, memory *mem)
{
    byte_t type = getByte(ptr, iter);
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
    return 1;
}

k_ptr_t SET::run(byte_t *ptr, k_ptr_t *iter, memory *mem)
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
    return 1;
}

k_ptr_t CPT::run(byte_t *ptr, k_ptr_t *iter, memory *mem)
{
    k_ptr_t dest = getPtr(ptr, iter);
    k_ptr_t targ = getPtr(ptr, iter);
    mem->set_addr(dest, targ);
    return 1;
}

k_ptr_t CPY::run(byte_t *ptr, k_ptr_t *iter, memory *mem)
{
    word_t sz = getWord(ptr, iter);
    k_ptr_t dest = getPtr(ptr, iter);
    k_ptr_t addr = getPtr(ptr, iter);
    for (word_t i = 0; i < sz; i++)
        mem->set_byte(dest, mem->get_byte(addr, i), i);
    return 1;
}

k_ptr_t ALC::run(byte_t *ptr, k_ptr_t *iter, memory *mem)
{
    k_ptr_t addr = getPtr(ptr, iter);
    word_t byte_count = getPtr(ptr, iter);
    mem->alloc(addr, byte_count);
    return 1;
}

k_ptr_t FRE::run(byte_t *ptr, k_ptr_t *iter, memory *mem)
{
    k_ptr_t addr = getPtr(ptr, iter);
    mem->free_mem(addr);
    return 1;
}

k_ptr_t RLC::run(byte_t *ptr, k_ptr_t *iter, memory *mem)
{
    k_ptr_t addr = getPtr(ptr, iter);
    word_t byte_count = getPtr(ptr, iter);
    mem->reallc(addr, byte_count);
    return 1;
}

k_ptr_t SUM::run(byte_t *ptr, k_ptr_t *iter, memory *mem)
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
    return 1;
}

k_ptr_t SUB::run(byte_t *ptr, k_ptr_t *iter, memory *mem)
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
    return 1;
}

k_ptr_t MUL::run(byte_t *ptr, k_ptr_t *iter, memory *mem)
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
    return 1;
}

k_ptr_t DIV::run(byte_t *ptr, k_ptr_t *iter, memory *mem)
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
    return 1;
}

k_ptr_t JMP::run(byte_t *ptr, k_ptr_t *iter, memory *mem)
{
    k_ptr_t addr = getPtr(ptr, iter);
    *iter = addr;
    return 1;
}

k_ptr_t JEQ::run(byte_t *ptr, k_ptr_t *iter, memory *mem)
{
    k_ptr_t arg0 = getPtr(ptr, iter);
    k_ptr_t arg1 = getPtr(ptr, iter);
    k_ptr_t addr = getPtr(ptr, iter);
    uint128_t v0 = mem->get_dec(arg0, mem->get_size(arg0));
    uint128_t v1 = mem->get_dec(arg1, mem->get_size(arg1));
    if (v0 == v1)
        *iter = addr;
    return 1;
}

k_ptr_t JGE::run(byte_t *ptr, k_ptr_t *iter, memory *mem)
{
    k_ptr_t arg0 = getPtr(ptr, iter);
    k_ptr_t arg1 = getPtr(ptr, iter);
    k_ptr_t addr = getPtr(ptr, iter);
    uint128_t v0 = mem->get_dec(arg0, mem->get_size(arg0));
    uint128_t v1 = mem->get_dec(arg1, mem->get_size(arg1));
    if (v0 >= v1)
        *iter = addr;
    return 1;
}

k_ptr_t JLE::run(byte_t *ptr, k_ptr_t *iter, memory *mem)
{
    k_ptr_t arg0 = getPtr(ptr, iter);
    k_ptr_t arg1 = getPtr(ptr, iter);
    k_ptr_t addr = getPtr(ptr, iter);
    uint128_t v0 = mem->get_dec(arg0, mem->get_size(arg0));
    uint128_t v1 = mem->get_dec(arg1, mem->get_size(arg1));
    if (v0 <= v1)
        *iter = addr;
    return 1;
}

k_ptr_t JG::run(byte_t *ptr, k_ptr_t *iter, memory *mem)
{
    k_ptr_t arg0 = getPtr(ptr, iter);
    k_ptr_t arg1 = getPtr(ptr, iter);
    k_ptr_t addr = getPtr(ptr, iter);
    uint128_t v0 = mem->get_dec(arg0, mem->get_size(arg0));
    uint128_t v1 = mem->get_dec(arg1, mem->get_size(arg1));
    if (v0 > v1)
        *iter = addr;
    return 1;
}

k_ptr_t JL::run(byte_t *ptr, k_ptr_t *iter, memory *mem)
{
    k_ptr_t arg0 = getPtr(ptr, iter);
    k_ptr_t arg1 = getPtr(ptr, iter);
    k_ptr_t addr = getPtr(ptr, iter);
    uint128_t v0 = mem->get_dec(arg0, mem->get_size(arg0));
    uint128_t v1 = mem->get_dec(arg1, mem->get_size(arg1));
    if (v0 < v1)
        *iter = addr;
    return 1;
}

k_ptr_t CALL::run(byte_t *ptr, k_ptr_t *iter, memory *mem)
{
    k_ptr_t call_addr = getPtr(ptr, iter);  // address of method
    word_t args = getWord(ptr, &call_addr); // count of args in method header
    for (k_ptr_t i = 0; i < args; i++)      // fill method vars with in args
    {
        k_ptr_t in_arg = getPtr(ptr, iter);       // input vars
        k_ptr_t me_arg = getPtr(ptr, &call_addr); // method vars
        mem->set_addr(me_arg, in_arg);
    }
    return call_addr;
}

k_ptr_t RET::run(byte_t *ptr, k_ptr_t *iter, memory *mem) { return 0; }