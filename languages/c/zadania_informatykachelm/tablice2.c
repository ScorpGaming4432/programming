#include <stdio.h>

int* wczytaj() {
    int out[255];
    int num = 0;
    unsigned char i = 0;
    printf("Podaj liczby do tabeli: (-1, ¿eby przerwaæ)\n");
    while(1) {
        scanf("%d", &num);
        if(num == -1) {
        	break;
		}
        out[i] = num;
        i++;
    }
    
    return out;
}

int main() {
    int *tab = wczytaj();
    printf("%d", tab);
}
