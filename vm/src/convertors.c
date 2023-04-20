#include "convertors.h"

int toInt(byte_t *ptr, byte_t n)
{
    int nm = ptr[0];
    for (byte_t i = 1; i < n; i++)
        nm += ptr[i] * (256 * i);
    return nm;
}

k_ptr_t toPtr(byte_t *ptr)
{
    k_ptr_t n = ptr[0];
    n += ptr[1] * 256;
    return n;
}

k_ptr_t getPtr(byte_t *ptr, uint_t *iter)
{
    k_ptr_t addr = toPtr(&ptr[*iter]);
    *iter += 2;
    return addr;
}