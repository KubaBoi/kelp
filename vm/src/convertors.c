#include "convertors.h"

int toInt(byte_t *ptr)
{
    int n = ptr[3];
    for (int i = 2; i >= 0; i--)
    {
        n += ptr[i] * (256 * (3 - i));
    }
    return n;
}

k_ptr_t toPtr(byte_t *ptr)
{
    k_ptr_t n = ptr[1];
    n += ptr[0] * 256;
    return n;
}

k_ptr_t getPtr(byte_t *ptr, uint_t *iter)
{
    k_ptr_t addr = toPtr(&ptr[*iter]);
    *iter += 2;
    return addr;
}