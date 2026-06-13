#ifndef HEXVIEWER_H
#define HEXVIEWER_H

#include <stddef.h>

int hexviewer_dump_file(const char *path, size_t line_length);

#ifdef HEX_VIEWER_IMPLEMENTATION
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>

int hexviewer_dump_file(const char *path, size_t line_length)
{
    FILE *fp;
    unsigned char *buf;
    size_t result;
    size_t i;
    unsigned long address;
    int err;

    if (path == NULL || line_length == 0)
        return EINVAL;

    fp = fopen(path, "rb");
    if (fp == NULL)
        return errno ? errno : EIO;

    buf = (unsigned char *)malloc(line_length);
    if (buf == NULL)
    {
        err = errno;
        fclose(fp);
        return err ? err : ENOMEM;
    }

    address = 0UL;
    result = fread(buf, 1, line_length, fp);
    while (result > 0)
    {
        printf("%08lx   ", address);
        for (i = 0; i < result; i++)
            printf("%02x ", (unsigned int)buf[i]);

        putchar('\n');
        address += (unsigned long)result;
        result = fread(buf, 1, line_length, fp);
    }

    if (ferror(fp))
    {
        err = errno;
        free(buf);
        fclose(fp);
        return err ? err : EIO;
    }

    free(buf);
    if (fclose(fp) != 0)
    {
        err = errno;
        return err ? err : EIO;
    }

    return 0;
}
#endif

#endif /* HEXVIEWER_H */
