#ifndef CONVERTORS_H
#define CONVERTORS_H

#include "type_defs.h"

int toInt(byte_t *ptr);

k_ptr_t toPtr(byte_t *ptr);

k_ptr_t getPtr(byte_t *ptr, uint_t *iter);

#endif