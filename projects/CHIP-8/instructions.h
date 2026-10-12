#pragma once
#include <stdint.h>


struct instruction
{
    const char *dissasembly;
    const char *raw;
    void *execute;
};

/// "name", "looks", function pointer

const struct instruction instructions[36] =
    {
        {"SYS addr", "0nnn", nullptr},
        {"CLS", "00E0", nullptr},
        {"RETURN", "00EE", nullptr},
        {"JUMP addr", "1nnn", nullptr},
        {"CALL addr", "2nnn", nullptr},
        {"SE Vx, byte", "3xkk", nullptr},
        {"SNE Vx, byte", "4xkk", nullptr},
        {"SE Vx, Vy", "5xy0", nullptr},
        {"LD Vx, byte", "6xkk", nullptr},
        {"ADD Vx, byte", "7xkk", nullptr},
        {"LD Vx, Vy", "8xy0", nullptr},
        {"OR Vx, Vy", "8xy1", nullptr},
        {"AND Vx, Vy", "8xy2", nullptr},
        {"XOR Vx, Vy", "8xy3", nullptr},
        {"ADD Vx, Vy", "8xy4", nullptr},
        {"SUB Vx, Vy", "8xy5", nullptr},
        {"SHR Vx {, Vy}", "8xy6", nullptr},
        {"SUBN Vx, Vy", "8xy7", nullptr},
        {"SHL Vx {, Vy}", "8xyE", nullptr},
        {"SNE Vx, Vy", "9xy0", nullptr},
        {"LD I, addr", "Annn", nullptr},
        {"JUMP V0 + addr", "Bnnn", nullptr},
        {"RND Vx, byte", "Cxkk", nullptr},
        {"DRW Vx, Vy, nibble", "Dxyn", nullptr},
        {"SKP Vx", "Ex9E", nullptr},
        {"SKNP Vx", "ExA1", nullptr},
        {"LD Vx, DT", "Fx07", nullptr},
        {"LD Vx, K", "Fx0A", nullptr},
        {"LD DT, Vx", "Fx15", nullptr},
        {"LD ST, Vx", "Fx18", nullptr},
        {"ADD I, Vx", "Fx1E", nullptr},
        {"LD F, Vx", "Fx29", nullptr},
        {"LD BCD, Vx", "Fx33", nullptr},
        {"LD [I], Vx", "Fx55", nullptr},
        {"LD Vx,[I]", "Fx65", nullptr}
    };
