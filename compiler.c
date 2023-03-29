
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef unsigned long ptr;

typedef struct
{
    char *name;
    char *line_content;
    char level;
    size_t line_index;
    size_t objects_count;
    size_t objects_size;

    ptr *objects; // array of objects inside this one
    ptr parent;   // parent of object
} object;

/**
 * Method allocates memory and return pointer
 * need to be freed
 *
 * return array of pointers to lines
 * first byte of line contains count of spaces before line content
 */
ptr *read_file(const char *path, size_t *sz)
{
    FILE *fl;
    fl = fopen(path, "r");
    *sz = 0;

    if (!fl)
    {
        printf("File not found");
        return 0;
    }

    size_t size = 100;
    unsigned int iter = 0;

    ptr *data_lines = (ptr *)malloc(size * sizeof(data_lines));
    while (!feof(fl))
    {
        char chr = fgetc(fl);
        long i = 1;
        long char_count = 100;
        char *line = (char *)malloc(char_count);
        char finding_level = 1;
        char level = 1;
        while (!feof(fl) && chr != '\n')
        {
            if (finding_level && chr == ' ')
                level++;
            if (finding_level && chr != ' ')
                finding_level = 0;

            if (i >= char_count)
            {
                char_count *= 2;
                line = (char *)realloc(line, char_count);
            }
            line[i++] = chr;
            chr = fgetc(fl);
        }
        line[0] = level;
        line[i] = 0;
        data_lines[iter++] = (ptr)line;
        if (iter >= size)
        {
            size *= 2;
            data_lines = (ptr *)realloc(data_lines, size);
            for (size_t j = iter; j < size; j++)
                data_lines[j] = 0;
        }
    }
    *sz = iter;
    return data_lines;
}

/**
 * Return pointer to line without first byte
 * and set value in `level` as that first byte
 *
 * If line is empty or contains python import of kelp
 * than return 0
 */
const char *get_line(ptr *data, char *level, size_t index)
{
    char *line = (char *)data[index];
    *level = 0;
    if (!(strlen(line) - line[0]))
        return 0;
    if (!strcmp(line + 1, "from kelp import *"))
        return 0;
    *level = line[0];
    return line + 1;
}

object *create_new_object(char *name, char level, char *line_cnt, size_t line_ind, object *prt)
{
    object *obj = (object *)malloc(sizeof(obj));
    obj->name = name;
    obj->level = level;
    obj->line_content = line_cnt;
    obj->line_index = line_ind;
    obj->parent = (ptr)prt;
    obj->objects_count = 0;
    obj->objects_size = 2;
    obj->objects = (ptr *)malloc(obj->objects_size * sizeof(ptr));
    obj->objects[0] = 0;
    return obj;
}

void add_object(object *obj)
{
    object *parent = (object *)obj->parent;
    parent->objects[parent->objects_count++] = (ptr)obj;
    if (parent->objects_count >= parent->objects_size)
    {
        parent->objects_size *= 2;
        parent->objects = (ptr *)realloc(parent->objects, parent->objects_size * sizeof(parent->objects));
        for (size_t i = parent->objects_count; i < parent->objects_size; i++)
            parent->objects[i] = 0;
    }
}

void print_object(object *obj)
{
    printf("%d %s", obj->level, obj->name);
    for (size_t i = 0; i < obj->objects_count; i++)
        print_object((object *)obj->objects[i]);
}

int main()
{
    size_t size;
    ptr *data = read_file("testApp.py", &size);
    if (!data)
        return 1;

    object *root = create_new_object("root", 0, 0, 0, 0);

    char old_level = 1;
    for (size_t i = 0; i < size; i++)
    {
        char level;
        const char *line = get_line(data, &level, i);
        if (!line)
            continue;
    }

    //print_object(root);

    for (size_t i = 0; i < size; i++)
        free((char *)data[i]);
    free(data);
}