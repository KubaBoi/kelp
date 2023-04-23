#ifndef MEMORY_H
#define MEMORY_H

#include <cstdlib>

#include "type_defs.h"

/**
 * mem_addr is address in mem
 *
 * addr is address in mem_map
 */
class memory
{
public:
    memory(k_ptr_t mem_map_sz);

    // Allocate bytes in memory and set mem_addr at addr
    void alloc(k_ptr_t addr, word_t bytes);

    // Return true if mem_addr at addr is not 0
    bool isAllocated(k_ptr_t addr);

    // Set byte into memory address with offset
    void setByte(k_ptr_t addr, byte_t byte, byte_t offset = 0);
    // Return 1 byte from addr
    byte_t getByte(k_ptr_t addr);
    // Return 2 bytes from addr
    word_t getWord(k_ptr_t addr);

private:
    k_ptr_t mem_iter;
    byte_t mem[100];

    k_ptr_t mem_map_sz;
    k_ptr_t *mem_map = nullptr;
};

#endif