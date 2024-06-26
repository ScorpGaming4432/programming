#include <stdio.h>

unsigned char parity(int num) {
    return num % 2;
}

int main(void) {
    int n;
    scanf("%d", &n);
    while(n) {
        printf("%c", parity(n));
        scanf("%d", &n);
    }
}