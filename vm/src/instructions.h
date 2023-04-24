#ifndef INSTRUCTIONS_H
#define INSTRUCTIONS_H

#include "type_defs.h"
#include "helpers.h"
#include "convertors.h"
#include "memory.h"

class instruction
{
public:
    virtual void run(byte_t *ptr, uint_t *iter, memory *mem);
};

class OUT : instruction
{
public:
    void run(byte_t *ptr, uint_t *iter, memory *mem);
};

class SET : instruction
{
public:
    void run(byte_t *ptr, uint_t *iter, memory *mem);
};

class SUM : instruction
{
public:
    void run(byte_t *ptr, uint_t *iter, memory *mem);
};

class SUB : instruction
{
public:
    void run(byte_t *ptr, uint_t *iter, memory *mem);
};

class MUL : instruction
{
public:
    void run(byte_t *ptr, uint_t *iter, memory *mem);
};

class DIV : instruction
{
public:
    void run(byte_t *ptr, uint_t *iter, memory *mem);
};

class CPY : instruction
{
public:
    void run(byte_t *ptr, uint_t *iter, memory *mem);
};

class ALC : instruction
{
public:
    void run(byte_t *ptr, uint_t *iter, memory *mem);
};

class FRE : instruction
{
public:
    void run(byte_t *ptr, uint_t *iter, memory *mem);
};

class RLC : instruction
{
public:
    void run(byte_t *ptr, uint_t *iter, memory *mem);
};

#endif