#include "memory.h"

memory::memory(k_ptr_t mem_map_sz)
{
    mem_iter = 1;
    this->mem_map_sz = mem_map_sz;

    mem = (byte_t *)malloc(100);
    mem_map = (k_ptr_t *)malloc(sizeof(mem_map) * mem_map_sz);
    for (k_ptr_t i = 0; i < mem_map_sz; i++)
        mem_map[i] = 0;
}

memory::~memory()
{
    free(mem);
    free(mem_map);
}

void memory::alloc(k_ptr_t addr, word_t bytes)
{
    mem_map[addr] = mem_iter;
    mem_iter += bytes;
}

bool memory::is_alloc(k_ptr_t addr) { return mem_map[addr]; }

void memory::set_byte(k_ptr_t addr, byte_t byte, byte_t offset)
{
    k_ptr_t mem_addr = mem_map[addr];
    if (!mem_addr)
        printf("%d: nullptr\n", addr);
    mem[mem_addr + offset] = byte;
}

byte_t memory::get_byte(k_ptr_t addr, byte_t offset)
{
    k_ptr_t mem_addr = mem_map[addr];
    return mem[mem_addr + offset];
}

word_t memory::get_word(k_ptr_t addr)
{
    return 0;
}

unsigned long long memory::get_dec(k_ptr_t addr, byte_t byte_count)
{
    k_ptr_t mem_addr = mem_map[addr];
    unsigned long long nm = mem[mem_addr];
    for (byte_t i = 0; i < byte_count; i++)
        nm += mem[mem_addr + i] * (256 * i);
    return nm;
}

void memory::prnt_mem()
{
}