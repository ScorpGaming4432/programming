#include <stdio.h>
#include <stdint.h>
#include "pbm.h"

#define HEIGHT 64
#define WIDTH  32


int main(int argc, char const *argv[])
{
    PBMImage * screen = new_pbmimage(WIDTH, HEIGHT);
    write_pbmfile(screen, "screen.pbm");
    return 0;
}
