#ifndef INSTRUCTIONS_H
#define INSTRUCTIONS_H

#include "type_defs.h"
#include "helpers.h"
#include "convertors.h"

void out(byte_t *ptr, uint_t *iter, byte_t *mem);

void set(byte_t *ptr, uint_t *iter, byte_t *mem, uint_t *mem_iter);

void sum(byte_t *ptr, uint_t *iter, byte_t *mem);

void sub(byte_t *ptr, uint_t *iter, byte_t *mem);

#endif