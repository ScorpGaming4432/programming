#include <stdio.h>

int main(int argc, char *argv[]) {
    // Check if enough arguments are provided
    if (argc < 3) {
        printf("Usage: %s input1 input2\n", argv[0]);
        return 1;
    }

    // Access the command-line arguments
    printf("Program name: %s\n", argv[0]);
    printf("First argument: %s\n", argv[1]);
    printf("Second argument: %s\n", argv[2]);

    // You can convert strings to integers or other types if needed
    // Example: int arg1 = atoi(argv[1]);

    return 0;
}
// gcc example.c -o example
//   this outputs the file to example.exe
// ./example inp1 inp2
//   run 'example' with 2 inputs


//this program wants 2 external inputs passed as the first one is always the program name