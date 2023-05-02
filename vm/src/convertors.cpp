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
    return (k_ptr_t)toInt(ptr, K_PTR_SIZE);
}

k_ptr_t getPtr(byte_t *ptr, k_ptr_t *iter)
{
    k_ptr_t addr = toPtr(&ptr[*iter]);
    *iter += K_PTR_SIZE;
    return addr;
}

word_t getWord(byte_t *ptr, k_ptr_t *iter) 
{
    word_t word = (word_t)toInt(&ptr[*iter], 2);
    *iter += 2;
    return word;
}

byte_t getByte(byte_t *ptr, k_ptr_t *iter) 
{
    byte_t byte = ptr[*iter];
    *iter += 1;
    return byte;
}