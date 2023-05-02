#ifndef INSTRUCTIONS_H
#define INSTRUCTIONS_H

#include "type_defs.h"
#include "helpers.h"
#include "convertors.h"
#include "memory.h"

class instruction
{
public:
    virtual k_ptr_t run(byte_t *ptr, k_ptr_t *iter, memory *mem);
};

class OUT : instruction
{
public:
    k_ptr_t run(byte_t *ptr, k_ptr_t *iter, memory *mem);
};

class SET : instruction
{
public:
    k_ptr_t run(byte_t *ptr, k_ptr_t *iter, memory *mem);
};

class CPT : instruction
{
public:
    k_ptr_t run(byte_t *ptr, k_ptr_t *iter, memory *mem);
};

class CPY : instruction
{
public:
    k_ptr_t run(byte_t *ptr, k_ptr_t *iter, memory *mem);
};

class ALC : instruction
{
public:
    k_ptr_t run(byte_t *ptr, k_ptr_t *iter, memory *mem);
};

class FRE : instruction
{
public:
    k_ptr_t run(byte_t *ptr, k_ptr_t *iter, memory *mem);
};

class RLC : instruction
{
public:
    k_ptr_t run(byte_t *ptr, k_ptr_t *iter, memory *mem);
};

class SUM : instruction
{
public:
    k_ptr_t run(byte_t *ptr, k_ptr_t *iter, memory *mem);
};

class SUB : instruction
{
public:
    k_ptr_t run(byte_t *ptr, k_ptr_t *iter, memory *mem);
};

class MUL : instruction
{
public:
    k_ptr_t run(byte_t *ptr, k_ptr_t *iter, memory *mem);
};

class DIV : instruction
{
public:
    k_ptr_t run(byte_t *ptr, k_ptr_t *iter, memory *mem);
};

class JMP : instruction
{
public:
    k_ptr_t run(byte_t *ptr, k_ptr_t *iter, memory *mem);
};

class JEQ : instruction
{
public:
    k_ptr_t run(byte_t *ptr, k_ptr_t *iter, memory *mem);
};

class JGE : instruction
{
public:
    k_ptr_t run(byte_t *ptr, k_ptr_t *iter, memory *mem);
};

class JLE : instruction
{
public:
    k_ptr_t run(byte_t *ptr, k_ptr_t *iter, memory *mem);
};

class JG : instruction
{
public:
    k_ptr_t run(byte_t *ptr, k_ptr_t *iter, memory *mem);
};

class JL : instruction
{
public:
    k_ptr_t run(byte_t *ptr, k_ptr_t *iter, memory *mem);
};

class CALL : instruction
{
public:
    k_ptr_t run(byte_t *ptr, k_ptr_t *iter, memory *mem);
};

class RET : instruction
{
public:
    k_ptr_t run(byte_t *ptr, k_ptr_t *iter, memory *mem);
};

#endif