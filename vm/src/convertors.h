#ifndef CONVERTORS_H
#define CONVERTORS_H

#include "type_defs.h"

// convert n bytes into integer
uint128_t toInt(byte_t *ptr, byte_t n);

// convert 2 bytes into pointer/short
k_ptr_t toPtr(byte_t *ptr);

// return next 2 bytes address from memory and moves iter
k_ptr_t getPtr(byte_t *ptr, k_ptr_t *iter);

// return next 2 bytes from memory and moves iter
word_t getWord(byte_t *ptr, k_ptr_t *iter);

// return value of next byte and move iter
byte_t getByte(byte_t *ptr, k_ptr_t *iter);

#endif