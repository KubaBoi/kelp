#ifndef CONVERTORS_H
#define CONVERTORS_H

#include "type_defs.h"

// convert n bytes into integer
int toInt(byte_t *ptr, byte_t n);

// convert 2 bytes into pointer/short
k_ptr_t toPtr(byte_t *ptr);

// return next 2 bytes address from memory and moves iter
k_ptr_t getPtr(byte_t *ptr, uint_t *iter);

// return value of next byte and move iter
byte_t getNextByte(byte_t *ptr, uint_t *iter);

#endif