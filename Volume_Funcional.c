#include <stdio.h>
    void volume_esfera(float r, float pi, float h) {
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

    float pi = 3.14;
    float r = 10;
    float h = 15;
    float area_base = 20;

   
   volume_esfera(r, pi, h);
   volume_piramide(area_base, h);
   volume_cilindro(r, pi, h);




    return 0;
}
