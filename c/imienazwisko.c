#include <stdio.h>

int main() {
    char imie[50];
    char nazwisko[50];
    scanf("%s", &imie);
    scanf("%s", &nazwisko);
    printf("Witaj użytkowniku %s %s\n", imie, nazwisko);
    return 0;
};
