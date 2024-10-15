#include <stdio.h>

float area_triangle(float a, float h); //pole trójkąta
float area_square(float a); //pole kwadratu
float area_circle(float r); //pole koła
float area_rect(float l, float w); //pole prostokąta
float area_rhombus(float d1, float d2); //pole rombu
float area_n(float n, float a);
float vol_sphere(float r); //objętość kuli
float vol_cone(float r, float h); //objętość stożka
float vol_cylinder(float r, float h); //objętość walca
float vol_cube(float a); //objętość sześcianu


int main() {
    char wybor;
    printf("Wybierz figurę:\n");
    printf("1. Trójkąt\n");
    printf("2. Kwadrat\n");
    printf("3. Koło\n");
    printf("4. Prostokąt\n");
    printf("5. Romb\n");
    printf("6. N-kąt foremny\n");
    printf("7. Kula\n");
    printf("9. Stożek\n");
    printf("10. Walec\n");
    printf("11. Sześcian\n");
    scanf("%u", &wybor);

    switch (wybor) {
        case 1: {
            float pods, wysok;
            printf("Podaj [długość podstawy, wysokość]: ");
            scanf("%f, %f", &pods, &wysok);
            printf("Pole trójkąta: %.3f\n", area_triangle(pods, wysok));
            break;
        }
        case 2: {
            float pods;
            printf("Podaj długość podstawy: ");
            scanf("%f", &pods);
            printf("Pole kwadratu: %.3f\n", area_square(pods));
            break;
        }
        case 3: {
            float promien;
            printf("Podaj promień: ");
            scanf("%f", &promien);
            printf("Pole koła: %.3f\n", area_circle(promien));
            break;
        }
        case 4: {
            float dlugosc, szerokosc;
            printf("Podaj [długość, szerokość]: ");
            scanf("%f, %f", &dlugosc, &szerokosc);
            printf("Pole prostokąta: %.3f\n", area_rect(dlugosc, szerokosc));
            break;
        }
        case 5: {
            float przekatna1, przekatna2;
            printf("Podaj [długość przekątnej 1, długość przekątnej 2]: ");
            scanf("%f, %f", &przekatna1, &przekatna2);
            printf("Pole rombu: %.3f\n", area_rhombus(przekatna1, przekatna2));
            break;
        }
        case 6: {
            unsigned int n;
            float dlugosc_boku;
            printf("Podaj [liczba boków, długość boku]: ");
            scanf("%u, %f", &n, &dlugosc_boku);
            printf("Pole n-kąta foremnego: %.3f\n", area_n(n, dlugosc_boku));
            break;
        }
        case 7: {
            float promien;
            printf("Podaj promień: ");
            scanf("%f", &promien);
            printf("Objętość kuli: %.3f\n", vol_sphere(promien));
            break;
        }
        case 8: {
            float promien;
            printf("Podaj promień: ");
            scanf("%f", &promien);
            printf("Objętość kuli: %.3f\n", vol_sphere(promien));
            break;
        }
        case 9: {
            float promien, wysokosc;
            printf("Podaj [promień, wysokość]: ");
            scanf("%f, %f", &promien, &wysokosc);
            printf("Objętość stożka: %.3f\n", vol_cone(promien, wysokosc));
            break;
        }
        case 10: {
            float promien, wysokosc;
            printf("Podaj [promień, wysokość]: ");
            scanf("%f, %f", &promien, &wysokosc);
            printf("Objętość walca: %.3f\n", vol_cylinder(promien, wysokosc));
            break;
        }
        case 11: {
            float bok;
            printf("Podaj długość boku: ");
            scanf("%f", &bok);
            printf("Objętość sześcianu: %.3f\n", vol_cube(bok));
            break;
        }
        default:
            printf("Nieprawidłowy wybór.\n");
            break;
    }

    return 0;
}

float area_triangle(float a, float h)
{
    return 0.5f * a * h;
}

float area_square(float a)
{
    return a * a;
}

float area_circle(float r)
{
    return 3.14159f * r * r;
}

float area_rect(float l, float w)
{
    return l * w;
}

float area_rhombus(float d1, float d2)
{
    return 0.5f * d1 * d2;
}

float area_n(float n, float a)
{
    #include <math.h>
    return n * a * a / (4 * tanf(3.14159f / n));
}

float vol_sphere(float r)
{
    return (4.0f/3.0f) * 3.14159f * r * r * r;
}

float vol_cone(float r, float h)
{
    return (1.0f/3.0f) * 3.14159f * r * r * h;
}

float vol_cylinder(float r, float h)
{
    return 3.14159f * r * r * h;
}

float vol_cube(float a)
{
    return a * a * a;
}

