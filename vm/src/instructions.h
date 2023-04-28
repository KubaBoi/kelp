#ifndef INSTRUCTIONS_H
#define INSTRUCTIONS_H

#include "type_defs.h"
#include "helpers.h"
#include "convertors.h"
#include "memory.h"

class instruction
{
public:
    virtual uint_t run(byte_t *ptr, uint_t *iter, memory *mem);
};

class OUT : instruction
{
public:
    uint_t run(byte_t *ptr, uint_t *iter, memory *mem);
};

class SET : instruction
{
public:
    uint_t run(byte_t *ptr, uint_t *iter, memory *mem);
};

class SUM : instruction
{
public:
    uint_t run(byte_t *ptr, uint_t *iter, memory *mem);
};

class SUB : instruction
{
public:
    uint_t run(byte_t *ptr, uint_t *iter, memory *mem);
};

class MUL : instruction
{
public:
    uint_t run(byte_t *ptr, uint_t *iter, memory *mem);
};

class DIV : instruction
{
public:
    uint_t run(byte_t *ptr, uint_t *iter, memory *mem);
};

class CPY : instruction
{
public:
    uint_t run(byte_t *ptr, uint_t *iter, memory *mem);
};

class ALC : instruction
{
public:
    uint_t run(byte_t *ptr, uint_t *iter, memory *mem);
};

class FRE : instruction
{
public:
    uint_t run(byte_t *ptr, uint_t *iter, memory *mem);
};

class RLC : instruction
{
public:
    uint_t run(byte_t *ptr, uint_t *iter, memory *mem);
};

class JMP : instruction
{
public:
    uint_t run(byte_t *ptr, uint_t *iter, memory *mem);
};

class JEQ : instruction
{
public:
    uint_t run(byte_t *ptr, uint_t *iter, memory *mem);
};

class JGE : instruction
{
public:
    uint_t run(byte_t *ptr, uint_t *iter, memory *mem);
};

class JLE : instruction
{
public:
    uint_t run(byte_t *ptr, uint_t *iter, memory *mem);
};

class JG : instruction
{
public:
    uint_t run(byte_t *ptr, uint_t *iter, memory *mem);
};

class JL : instruction
{
public:
    uint_t run(byte_t *ptr, uint_t *iter, memory *mem);
};

class CALL : instruction
{
public:
    uint_t run(byte_t *ptr, uint_t *iter, memory *mem);
};

class RET : instruction
{
public:
    uint_t run(byte_t *ptr, uint_t *iter, memory *mem);
};

#endif