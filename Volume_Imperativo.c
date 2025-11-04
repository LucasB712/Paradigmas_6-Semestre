#include <stdio.h>
int main() {

    float pi = 3.14;
    float r = 10;
    float h = 15;
    float area_base = 20;

         float volume_esfera = 4 * pi * r * r * r/ 3;
      

        float volume_piramide = area_base * h / 3;
        

         float volume_cilindro = pi * r * r * h;


        printf("%f \n", volume_esfera);
        printf("%f \n", volume_piramide);
        printf("%f \n", volume_cilindro);

    return 0;
}
