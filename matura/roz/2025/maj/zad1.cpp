#include <stdint.h>

uint64_t przestaw(uint64_t number) {
    uint8_t current = number % 100;
    uint8_t right = current / 10;
    uint8_t left = current % 10;
    number = number / 100;
    uint64_t result = 0; // Initialize result

    if (number > 0) {
        result = 100 * przestaw(number) + 10 * left + right;
    } else {
        if (right > 0) {
            result = right + 10 * left;
        } else {
            result = left;
        }
    }
    return result;
}

int main() {
    return 0;
}