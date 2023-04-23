#ifndef INSTRUCTIONS_H
#define INSTRUCTIONS_H

#include "type_defs.h"
#include "helpers.h"
#include "convertors.h"
#include "memory.h"

void out(byte_t *ptr, uint_t *iter, memory *mem);

void set(byte_t *ptr, uint_t *iter, memory *mem);

void sum(byte_t *ptr, uint_t *iter, memory *mem);

void sub(byte_t *ptr, uint_t *iter, memory *mem);

void mul(byte_t *ptr, uint_t *iter, memory *mem);

void div(byte_t *ptr, uint_t *iter, memory *mem);

void cpy(byte_t *ptr, uint_t *iter, memory *mem);

#endif