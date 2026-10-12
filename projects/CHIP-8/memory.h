#pragma once
#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "registers.h"

#define START_RAM 0x000
#define START_CHIP8 0x200
#define START_ETI660 0x600
#define END_RAM 0xFFF

void* RAM;

int init_RAM() {
    RAM = malloc(END_RAM);
    return RAM != NULL;
}

void load_game_to_ram(const char* game, size_t size) {
    if (size > END_RAM - START_CHIP8) {
        fprintf(stderr, "Game size exceeds available RAM space.\n");
        exit(EXIT_FAILURE);
    }
    memcpy((uint8_t*)RAM + START_CHIP8, fopen(game, "r"), size);
}

int free_RAM() {
    free(RAM);
    return 0;
}

uint16_t read() {
    PC += 2;
    return *(uint16_t*)((uint8_t*)RAM + PC - 2);
}