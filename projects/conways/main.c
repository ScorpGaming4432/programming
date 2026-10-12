#include <stdint.h>
#include <stdio.h>

#define SIZE_X 50
#define SIZE_Y 60

void print_map(uint8_t map[SIZE_Y][SIZE_X])
{
    size_t i, j;
    for (i = 0; i < SIZE_Y; i++)
    {
        for (j = 0; j < SIZE_X; j++)
        {
            printf("%u", map[i][j]);
        }
        printf("\n");
    }
}

int main(int argc, char const *argv[])
{
    uint8_t map[SIZE_Y][SIZE_X] = {0};
    // printf("0x%x", map);
    print_map(map);
    return 0;
}

unsigned long long *(*(*(*(*(*(*(*(*arr[3])(double, const char *))[5])(int))[7])(float, long))[11])(void))[13];
const unsigned long long *(*(*(*(*(*(*(*(*arr[3])(const double *const precision, const char *))[5])(signed int**))[7])(float, long long))[10])(void**))[13];
