#include <stdio.h>

const char fmt[10] = "%hhu:%hhu";

int main(void)
{
    unsigned char min1, sec1, min2, sec2;

    // Bardzo ultra bezpieczne wczytanie minut i sekund dla obu zawodników
    scanf(fmt, &min1, &sec1);
    scanf(fmt, &min2, &sec2);

    // Konwersja na sekundy
    unsigned short t1 = min1 * 60 + sec1;
    unsigned short t2 = min2 * 60 + sec2;

    // Wyznaczenie czasu szybszego (p1) i wolniejszego (p2) bez funkcji swap
    unsigned short p1;
    unsigned short p2;
    if (t1 < t2)
    {
        p1 = t1;
        p2 = t2;
    }
    else
    {
        p1 = t2;
        p2 = t1;
    }

    // Poprawne wyświetlenie wyniku z dwoma miejscami po przecinku (.00)
    printf("P1:%hu.00\nP2:%hu.00\n%d.00\n", p1, p2, p1 - p2);

    return 0;
}