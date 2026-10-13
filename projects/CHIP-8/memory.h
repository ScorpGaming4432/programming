#pragma once
#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "registers.h"
#include "instructions.h"

#define START_RAM 0x000
#define START_CHIP8 0x200
#define START_ETI660 0x600
#define END_RAM 0xFFF

void *RAM;

#define RAM_SIZE 0x1000

int init_RAM(void)
{
    RAM = calloc(RAM_SIZE, 1);
    return RAM != NULL;
}

void load_game_to_ram(const char *game, size_t size)
{
    if (size > RAM_SIZE - START_CHIP8)
    {
        fprintf(stderr, "Game size exceeds available RAM space.\n");
        exit(EXIT_FAILURE);
    }

    FILE *file = fopen(game, "rb");
    if (file == NULL)
    {
        perror(game);
        exit(EXIT_FAILURE);
    }

    size_t bytes_read = fread((uint8_t *)RAM + START_CHIP8, 1, size, file);
    if (bytes_read != size)
    {
        fprintf(stderr, "Could not read the entire game file.\n");
        fclose(file);
        exit(EXIT_FAILURE);
    }

    fclose(file);
}

int free_RAM()
{
    free(RAM);
    return 0;
}

void read()
{
    if (PC >= END_RAM)
    {
        fprintf(stderr, "PC REACHED EOF");
        exit(1);
    }

    uint8_t *ram = (uint8_t *)RAM;
    read_output = ((uint16_t)ram[PC] << 8) | ram[PC + 1];
    PC += 2;
}

void execute(void)
{
    const size_t instruction_count = sizeof(instructions) / sizeof(instructions[0]);
    for (size_t index = 0; index < instruction_count; index++)
    {
        const struct instruction *instruction = &instructions[index];
        if ((read_output & instruction->mask) == instruction->value)
        {
            if (instruction->execute == nullptr)
            {
                fprintf(stderr, "Instruction not implemented: %s (%04X)\n", instruction->dissasembly, read_output);
                exit(1);
                return;
            }

            instruction->execute();
            printf("%04hx | %s\n", read_output, instruction->dissasembly);
            return;
        }
    }

    fprintf(stderr, "Unknown opcode: %04X\n", read_output);
}