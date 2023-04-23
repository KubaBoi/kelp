#ifndef MEMORY_H
#define MEMORY_H

#include <cstdlib>

#include "type_defs.h"
#include <stdio.h>

/**
 * mem_addr is address in mem
 *
 * addr is address in mem_map
 */
class memory
{
public:
    memory(k_ptr_t mem_map_sz);
    ~memory();

    // Allocate bytes in memory and set mem_addr at addr
    void alloc(k_ptr_t addr, word_t bytes);

    // Return true if mem_addr at addr is not 0
    bool is_alloc(k_ptr_t addr);

    // Set byte into memory address with offset
    void set_byte(k_ptr_t addr, byte_t byte, byte_t offset = 0);
    // Return 1 byte from addr
    byte_t get_byte(k_ptr_t addr, byte_t offset = 0);
    // Return 2 bytes from addr
    word_t get_word(k_ptr_t addr);
    // Convert `byte_count` of bytes into ULL
    unsigned long long get_dec(k_ptr_t addr, byte_t byte_count);

    void prnt_mem();

private:
    k_ptr_t mem_iter;
    byte_t *mem;

    k_ptr_t mem_map_sz;
    k_ptr_t *mem_map;
};

#endif