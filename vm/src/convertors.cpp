#include "convertors.h"

uint128_t toInt(byte_t *ptr, byte_t n)
{
    uint128_t nm = ptr[0];
    for (byte_t i = 1; i < n; i++)
        nm += ptr[i] * (256 * i);
    return nm;
}

k_ptr_t toPtr(byte_t *ptr)
{
    return (k_ptr_t)toInt(ptr, 2);
}

k_ptr_t getPtr(byte_t *ptr, uint_t *iter)
{
    k_ptr_t addr = toPtr(&ptr[*iter]);
    *iter += 2;
    return addr;
}


byte_t getNextByte(byte_t *ptr, uint_t *iter) 
{
    byte_t byte = ptr[*iter];
    *iter += 1;
    return byte;
}