#include <stdio.h>

int main() {
    char wybor;
    printf("KtÛro zadanie? \n");
    scanf("%u", &wybor);
    
    float input;
    switch (wybor)
    {
    case 1:
        printf("PODAJ D£UGOå∆ WYRAØON•Ñ W CALACH : ");
        scanf("%f", &input);
        printf("D≈ÅUGOå∆ W CM : %.2f", input * 2.54f);
        break;
    case 2:
        printf("PODAJ ILE Z£OT”WEK: ");
        scanf("%f", &input);
        printf("ILOå∆ W USD: %.3f", input * 3.92f);
        break;
    case 3:
        printf("PODAJ TEMP W CELCJUSZACH: ");
        scanf("%f", &input);
        printf("TEMP W FARENHEITACH: %.2f",  (9 * input/5.0f) + 32.0f);
        break;
    case 4:
        printf("PODAJ ILOå∆ W LITRACH: ");
        scanf("%f", &input);
        printf("ILOå∆ W GALONACH: %.2f", input * 0.264172);
        break;
    default:
        break;
    }
    return 0;
}
