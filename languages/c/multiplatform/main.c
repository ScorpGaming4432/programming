#include <stdio.h>
#include "info.h"

int main(void)
{
    printf("Language: %s\n", INFO.language);
    printf("Standard: %d\n", INFO.standard);
    printf("Compiler: %s\n", INFO.compiler);
    printf("OS: %s\n", INFO.operating_system);

    return 0;
}