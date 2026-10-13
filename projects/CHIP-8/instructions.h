#pragma once
#include <stdint.h>
#include <stdio.h>
#include "registers.h"

typedef void (*instruction_handler)(void);

struct instruction
{
    const char *dissasembly;
    const char *raw;
    uint16_t mask;
    uint16_t value;
    instruction_handler execute;
};

void CLS(void) {
    
}

// void DRW_Vx_Vy_n(uint16_t read_output) {
//     /*Display n-byte sprite starting at memory location I at (Vx, Vy), set VF = collision.

//     The interpreter reads n bytes from memory, starting at the address stored in I. These bytes are then displayed as sprites on screen at coordinates (Vx, Vy). Sprites are XORed onto the existing screen. If this causes any pixels to be erased, VF is set to 1, otherwise it is set to 0. If the sprite is positioned so part of it is outside the coordinates of the display, it wraps around to the opposite side of the screen. See instruction 8xy3 for more information on XOR, and section 2.4, Display, for more information on the Chip-8 screen and sprites.*/
//     uint8_t n = read_output & 0x000F;
//     printf("%*x", n, I);
// }

void LD_I_addr(void) {
    I = read_output & 0x0FFF;
}

void LD_VX_byte(void) {
    uint8_t x = (read_output >> 8) & 0x000F;
    uint8_t kk = read_output & 0x00FF;
    V[x] = kk;
    
}


/// "name", "looks", function pointer

const struct instruction instructions[] =
    {
        {"CLS", "00E0", 0xFFFF, 0x00E0, nullptr},
        {"RETURN", "00EE", 0xFFFF, 0x00EE, nullptr},
        {"SYS addr", "0nnn", 0xF000, 0x0000, nullptr},
        {"JUMP addr", "1nnn", 0xF000, 0x1000, nullptr},
        {"CALL addr", "2nnn", 0xF000, 0x2000, nullptr},
        {"SE Vx, byte", "3xkk", 0xF000, 0x3000, nullptr},
        {"SNE Vx, byte", "4xkk", 0xF000, 0x4000, nullptr},
        {"SE Vx, Vy", "5xy0", 0xF00F, 0x5000, nullptr},
        {"LD Vx, byte", "6xkk", 0xF000, 0x6000, LD_VX_byte},
        {"ADD Vx, byte", "7xkk", 0xF000, 0x7000, nullptr},
        {"LD Vx, Vy", "8xy0", 0xF00F, 0x8000, nullptr},
        {"OR Vx, Vy", "8xy1", 0xF00F, 0x8001, nullptr},
        {"AND Vx, Vy", "8xy2", 0xF00F, 0x8002, nullptr},
        {"XOR Vx, Vy", "8xy3", 0xF00F, 0x8003, nullptr},
        {"ADD Vx, Vy", "8xy4", 0xF00F, 0x8004, nullptr},
        {"SUB Vx, Vy", "8xy5", 0xF00F, 0x8005, nullptr},
        {"SHR Vx {, Vy}", "8xy6", 0xF00F, 0x8006, nullptr},
        {"SUBN Vx, Vy", "8xy7", 0xF00F, 0x8007, nullptr},
        {"SHL Vx {, Vy}", "8xyE", 0xF00F, 0x800E, nullptr},
        {"SNE Vx, Vy", "9xy0", 0xF00F, 0x9000, nullptr},
        {"LD I, addr", "Annn", 0xF000, 0xA000, LD_I_addr},
        {"JUMP V0 + addr", "Bnnn", 0xF000, 0xB000, nullptr},
        {"RND Vx, byte", "Cxkk", 0xF000, 0xC000, nullptr},
        {"DRW Vx, Vy, nibble", "Dxyn", 0xF000, 0xD000, nullptr},
        {"SKP Vx", "Ex9E", 0xF0FF, 0xE09E, nullptr},
        {"SKNP Vx", "ExA1", 0xF0FF, 0xE0A1, nullptr},
        {"LD Vx, DT", "Fx07", 0xF0FF, 0xF007, nullptr},
        {"LD Vx, K", "Fx0A", 0xF0FF, 0xF00A, nullptr},
        {"LD DT, Vx", "Fx15", 0xF0FF, 0xF015, nullptr},
        {"LD ST, Vx", "Fx18", 0xF0FF, 0xF018, nullptr},
        {"ADD I, Vx", "Fx1E", 0xF0FF, 0xF01E, nullptr},
        {"LD F, Vx", "Fx29", 0xF0FF, 0xF029, nullptr},
        {"LD BCD, Vx", "Fx33", 0xF0FF, 0xF033, nullptr},
        {"LD [I], Vx", "Fx55", 0xF0FF, 0xF055, nullptr},
        {"LD Vx,[I]", "Fx65", 0xF0FF, 0xF065, nullptr}
    };


