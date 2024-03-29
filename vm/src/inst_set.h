#ifndef INST_SET_H
#define INST_SET_H
#define INST_SET_SIZE 16

#include "instructions.h"

uintptr_t inst_set[INST_SET_SIZE] = {
    (uintptr_t) new OUT(),
    (uintptr_t) new SET(),
    (uintptr_t) new CPT(),
    (uintptr_t) new CPY(),
    (uintptr_t) new ALC(),
    (uintptr_t) new FRE(),
    (uintptr_t) new RLC(),
    (uintptr_t) new SUM(),
    (uintptr_t) new SUB(),
    (uintptr_t) new MUL(),
    (uintptr_t) new DIV(),
    (uintptr_t) new CALL(),
    (uintptr_t) new RET(),
    (uintptr_t) new JMP(),
    (uintptr_t) new JMC()};
#endif