#ifndef MEMORY_H
#define MEMORY_H

#include <cstdlib>
#include <stdio.h>
#include <stdint.h>

#include "type_defs.h"

/**
 * memory is partitioned into segments
 * 
 * there is n segments and it is defined as the
 * first 2 bytes of bytecode
 * 
 * every segment can hold various count of bytes
 * and its size is stored at same address in sizes array
 */
class memory
{
public:
    memory(k_ptr_t mem_sz);
    ~memory();

    // Allocate bytes in memory and set mem_addr at addr
    void alloc(k_ptr_t addr, word_t bytes);

    // Free bytes from memory
    void free_mem(k_ptr_t addr);

    // Realloc to new bytes size
    void reallc(k_ptr_t addr, word_t bytes);

    // Return true if mem_addr at addr is not 0
    bool is_alloc(k_ptr_t addr);

    // Return mem pointer
    byte_t *get_mem(k_ptr_t addr);

    // Set byte into memory address with offset
    void set_byte(k_ptr_t addr, byte_t byte, word_t offset = 0);
    // Return 1 byte from addr
    byte_t get_byte(k_ptr_t addr, word_t offset = 0);
    // return byte_t pointer
    byte_t *get_bytes(k_ptr_t addr);
    // Return byte_t pointer and size of memory part in size
    byte_t *get_bytes(k_ptr_t addr, word_t *size);
    // Convert `byte_count` of bytes into ULL
    unsigned long long get_dec(k_ptr_t addr, byte_t byte_count);

    void prnt_mem();
    void prnt_mem_adv();

private:
    k_ptr_t mem_sz;
    uintptr_t *mem;
    word_t *sizes;
};

#endif