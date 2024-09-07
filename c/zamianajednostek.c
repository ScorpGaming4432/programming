#include <stdio.h>

float in_to_cm(float inch) {
    return inch * 2.54; //1 inch =  2.54cm
}

int main() {
    printf("%d", sizeof(double));
    float in;

    printf("Enter a value in inches: ");
    scanf("%f", &in);

    printf("%.2f inches is %.2f centimeters\n", in, in_to_cm(in));

    return 0;
}