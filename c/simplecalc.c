#include <stdio.h>

unsigned char parity(int num) {
    return !num % 2;
}

int main(void) {
    int n;
    scanf("%d", &n);
    printf("%d", parity(n));
    return 0;
}
