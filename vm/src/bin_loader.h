#ifndef BIN_LOADER_H
#define BIN_LOADER_H

#include <stdio.h>
#include <cstdlib>

#include "type_defs.h"

class binloader
{
public:
    static byte_t *getSourceFromFile(const char *path);
};

#endif