#include "memory.h"

memory::memory(k_ptr_t mem_map_sz)
{
    mem_iter = 1;
    this->mem_map_sz = mem_map_sz;
    mem_map = (k_ptr_t *)malloc(sizeof(mem_map) * mem_map_sz);
    for (k_ptr_t i = 0; i < mem_map_sz; i++)
        mem_map[i] = 0;
}

void memory::alloc(k_ptr_t addr, word_t bytes)
{
    mem_map[addr] = mem_iter;
    mem_iter += bytes;
}

bool memory::isAllocated(k_ptr_t addr) { return mem_map[addr]; }

void memory::setByte(k_ptr_t addr, byte_t byte, byte_t offset)
{
    k_ptr_t mem_addr = mem_map[addr];
    mem[mem_addr + offset] = byte;
}

byte_t memory::getByte(k_ptr_t addr)
{
    k_ptr_t mem_addr = mem_map[addr];
    return mem[mem_addr];
}

word_t memory::getWord(k_ptr_t addr)
{
    return 0;
}