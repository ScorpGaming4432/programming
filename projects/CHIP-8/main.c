#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#include "instructions.h"
#include "memory.h"
#include "registers.h"

// Source - https://stackoverflow.com/a/8247
// Posted by Derek Park, modified by community. See post 'Timeline' for change history
// Retrieved 2026-10-13, License - CC BY-SA 3.0

unsigned long fsize(const char* file)
{
    FILE * f = fopen(file, "r");
    fseek(f, 0, SEEK_END);
    unsigned long len = (unsigned long)ftell(f);
    fclose(f);
    return len;
}


int init(const char* game_name) {
    init_RAM();
    load_game_to_ram(game_name, fsize(game_name));
    PC = START_CHIP8;
    return 0;
}

int main(int argc, char const *argv[])
{   
    const uint32_t FILE_SIZE = fsize(argv[1]);
    init(argv[1]);
    // PC = 0; // testing
    while (1) {
        read();
        execute();
    }
}
