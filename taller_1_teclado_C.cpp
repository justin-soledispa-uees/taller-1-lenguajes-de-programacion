#include <stdio.h>
#include <time.h>

int main() {
    clock_t inicio = clock();
    
    int suma = 0;
    int contador = 1;
    int valor;

    while (contador <= 10) {
        printf("Ingrese el valor %d: ", contador);
        scanf("%d", &valor);
        suma += valor;
        contador++;
    }

    float promedio = (float)suma / 10;
    printf("Suma: %d, Promedio: %.2f\n", suma, promedio);


    clock_t fin = clock();
    double total = (double)(fin - inicio) / CLOCKS_PER_SEC;

    printf("\nTiempo %.3f segundos\n", total);

    return 0;
}