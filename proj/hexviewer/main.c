#define HEX_VIEWER_IMPLEMENTATION
#include "hexviewer.h"
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>

int main(int argc, char const *argv[])
{
    char *endptr;
    unsigned long tmp;

    if (argc < 3)
    {
        fprintf(stderr, "Usage: %s <file> <bytes-per-line>\n", argv[0]);
        return EINVAL;
    }
    if (argc > 3)
    {
        fprintf(stderr, "Too many arguments\n");
        return E2BIG;
    }

    errno = 0;
    tmp = strtoul(argv[2], &endptr, 10);
    if (errno == ERANGE)
    {
        fprintf(stderr, "Length out of range: %s\n", argv[2]);
        return ERANGE;
    }
    if (endptr == argv[2] || *endptr != '\0')
    {
        fprintf(stderr, "Invalid length: %s\n", argv[2]);
        return EINVAL;
    }
    if (tmp == 0UL)
    {
        fprintf(stderr, "Length must be > 0\n");
        return EINVAL;
    }
    if (tmp > 1024UL * 1024UL)
    {
        fprintf(stderr, "Requested length too large\n");
        return E2BIG;
    }

    return hexviewer_dump_file(argv[1], (size_t)tmp);
}
