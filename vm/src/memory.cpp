#include "memory.h"

memory::memory(k_ptr_t mem_sz)
{
    this->mem_sz = mem_sz;
    mem = (uintptr_t *)malloc(sizeof(mem) * mem_sz);
    sizes = (word_t *)malloc(sizeof(sizes) * mem_sz);
    for (k_ptr_t i = 0; i < mem_sz; i++)
    {
        mem[i] = 0;
        sizes[i] = 0;
    }
}

memory::~memory()
{
    for (k_ptr_t i = 0; i < mem_sz; i++)
        if (mem[i])
            delete (byte_t *)mem[i];
    delete mem;
    delete sizes;
}

void memory::alloc(k_ptr_t addr, word_t bytes)
{
    mem[addr] = (uintptr_t)malloc(bytes);
    sizes[addr] = bytes;
}

void memory::free_mem(k_ptr_t addr)
{
    delete (byte_t *)mem[addr];
    mem[addr] = 0;
    sizes[addr] = 0;
}

void memory::reallc(k_ptr_t addr, word_t bytes)
{
    byte_t *mem_addr = (byte_t *)mem[addr];
    mem[addr] = (uintptr_t)realloc(mem_addr, bytes);
    sizes[addr] = bytes;
}

bool memory::is_alloc(k_ptr_t addr) { return mem[addr]; }

byte_t *memory::get_mem(k_ptr_t addr) { return (byte_t *)mem[addr]; }

void memory::set_byte(k_ptr_t addr, byte_t byte, word_t offset)
{
    byte_t *mem_addr = (byte_t *)mem[addr];
    mem_addr[offset] = byte;
}

byte_t memory::get_byte(k_ptr_t addr, word_t offset)
{
    byte_t *mem_addr = (byte_t *)mem[addr];
    return mem_addr[offset];
}

byte_t *memory::get_bytes(k_ptr_t addr) { return (byte_t *)mem[addr]; }

byte_t *memory::get_bytes(k_ptr_t addr, word_t *size)
{
    *size = sizes[addr];
    return (byte_t *)mem[addr];
}

word_t memory::get_size(k_ptr_t addr) { return sizes[addr]; }

uint128_t memory::get_dec(k_ptr_t addr, byte_t byte_count)
{
    byte_t *mem_addr = (byte_t *)mem[addr];
    uint128_t nm = mem_addr[0];
    for (byte_t i = 0; i < byte_count; i++)
        nm += mem_addr[i] * (256 * i);
    return nm;
}

void memory::prnt_mem()
{
    printf("\nMEM:\n");
    for (word_t addr = 0; addr < mem_sz; addr++)
    {
        byte_t *mem_addr = (byte_t *)mem[addr];
        printf("%d (%d b): ", addr, sizes[addr]);
        if (mem_addr)
        {
            for (word_t bt = 0; bt < sizes[addr]; bt++)
                printf("%d ", mem_addr[bt]);
        }
        printf("\n");
    }
}

void memory::prnt_mem_adv() 
{
    printf("\nMEM:\n");
    for (word_t addr = 0; addr < mem_sz; addr++)
    {
        byte_t *mem_addr = (byte_t *)mem[addr];
        printf("%d (%d b): ", addr, sizes[addr]);
        if (mem_addr)
        {
            for (word_t bt = 0; bt < sizes[addr]; bt++)
                printf("%d[%c] ", mem_addr[bt], mem_addr[bt]);
        }
        printf("\n");
    }
}