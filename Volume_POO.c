#include <stdio.h>

 typedef struct {
        float pi;
        float r;
    } Esfera;

    typedef struct {
        float area_base;
        float h;
    } Piramide;
    
    typedef struct {
        float pi;
        float r;
        float h;
    } Cilindro;


    void volume_esfera(float r, float pi) {
        float volume = 4 * pi * r * r * r/ 3;
        printf("%f \n", volume);
    }

    void volume_piramide(float area_base, float h) {
        float volume = area_base * h / 3;
        printf("%f \n", volume);
    }
    void volume_cilindro(float r, float pi, float h) {
        float volume = pi * r * r * h;
        printf("%f \n", volume);
    }

int main() {

   Esfera e;
   Piramide p;
   Cilindro c;

   e.pi = 3.14;
   c.pi = 3.14;

   e.r = 10;
   p.area_base = 5;
   p.h = 7;
   c.r = 10;
   c.h = 12;

   
   volume_esfera(e.r, e.pi);
   volume_piramide(p.area_base, p.h);
   volume_cilindro(c.r, c.pi, c.h);




    return 0;
}
