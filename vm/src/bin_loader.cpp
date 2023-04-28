#include "bin_loader.h"

byte_t *binloader::getSourceFromFile(const char *path)
{
    FILE *src_file;
    char ch;
    src_file = fopen(path, "r");

    size_t i = 0;
    size_t sz = 100;
    byte_t *source = (byte_t *)malloc(sz);

    do
    {
        if (i >= sz)
        {
            sz *= 2;
            source = (byte_t *)realloc(source, sz);
        }
        ch = fgetc(src_file);
        source[i++] = ch;
    } while (ch != EOF);
    fclose(src_file);
    return source;
}