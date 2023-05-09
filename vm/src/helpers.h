#ifndef HELPERS_H
#define HELPERS_H

#include <stdio.h>

#include "type_defs.h"

void printMem(byte_t *mem, uint_t mem_iter);

void printBits(size_t const size, void const *const ptr);

void toCharArray(size_t const size, ptr_t ptr, byte_t *trg);

void moduloByTwo(byte_t num, byte_t *modulo, byte_t *div);

#endif