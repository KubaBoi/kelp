#include "helpers.h"

void printMem(byte_t *mem, uint_t mem_iter)
{
    printf("MEM: ");
    for (uint_t i = 0; i < mem_iter; i++)
        printf("%d ", mem[i]);
    printf("\n");
}

void printBits(size_t const size, void const *const ptr)
{
    unsigned char *b = (unsigned char *)ptr;
    unsigned char byte;
    int i, j;

    for (i = size - 1; i >= 0; i--)
    {
        for (j = 7; j >= 0; j--)
        {
            byte = (b[i] >> j) & 1;
            printf("%u", byte);
        }
        printf(" ");
    }
    puts("");
}

void toCharArray(size_t size, ptr_t ptr, byte_t *trg)
{
    for (size_t i = 0; i < size; i++)
        trg[i] = (byte_t)(ptr >> (8 * i));
}

void moduloByTwo(byte_t num, byte_t *modulo, byte_t *div)
{
    *modulo = (num & ( 1 << 7) >> 7);
    *div = num >> 1;
}