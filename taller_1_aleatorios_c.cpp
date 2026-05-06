#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(NULL));

    int pares = 0;
    int impares = 0;
    int num;

    for (int i = 0; i < 500; i++) {
        num = (rand() % (100 - 50 + 1)) + 50;

        if (num % 2 == 0) {
            pares++;
        } else {
            impares++;
        }
    }

    printf("Total pares : %d\n", pares);
    printf("Total impares : %d\n", impares);

    return 0;
}