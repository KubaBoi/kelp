
#include <stdio.h>
#include <cstdlib>

typedef unsigned long ptr_t;
typedef unsigned short k_ptr_t; // pointer in kelp lang
typedef unsigned char byte_t;
typedef unsigned int uint_t;

/**
 * Instruction
 * - 1 byte - code
 * - 2 byte - address to value ... every code has different count of parameters
 */

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

void toCharArray(size_t const size, ptr_t ptr, byte_t *trg)
{
    for (int i = 0; i < size; i++)
        trg[i] = (byte_t)(ptr >> (8 * i));
}

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

void set(byte_t *ptr, uint_t *iter, byte_t *mem, uint_t *mem_iter) 
{
    byte_t sz = ptr[*iter];
    *iter += 1;
    sz += *iter;
    while (*iter < sz) {
        mem[*mem_iter] = ptr[*iter];
        *iter += 1;
        *mem_iter += 1;
    }
}

void sum(byte_t *ptr, uint_t *iter, byte_t *mem) 
{
    k_ptr_t addr1 = toPtr(&ptr[*iter]); *iter;
    *iter += 2;
    k_ptr_t addr2 = toPtr(&ptr[*iter]); *iter;
    *iter += 2;
    int result = mem[addr1] + mem[addr2];
    printf("%d + %d = %d\n", mem[addr1], mem[addr2], result);
}

byte_t source[15] = {
    0, 0, 0, 15,  // first 4 bytes are size of array
    1, 1, 5,      // SET 1 byte as 5
    1, 1, 4,      // SET 1 byte as 4
    2, 0, 0, 0, 1 // SUM value at addres 0 and 1
};

byte_t mem[100];

int main()
{
    for (int i = 0; i < 100; i++)
        mem[i] = 0;

    uint_t size = toInt(source);

    uint_t mem_iter = 0;
    uint_t iter = 4;
    while (iter < size)
    {
        byte_t inst = source[iter++];
        printf("%u INST: %d\n", iter, inst);
        printf("MEM: ");
        for (int i = 0; i < mem_iter; i++)
            printf("%d ", mem[i]);
        printf("\n");
        
        if (inst == 1) // SET
        {
            set(source, &iter, mem, &mem_iter);
        }
        else if (inst == 2) // SUM
        {
            sum(source, &iter, mem);
        }
    }
}