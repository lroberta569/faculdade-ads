#include <stdio.h>
#include <stdlib.h> 

int* gerarRandomico();

int main() {
    int* randomicos = gerarRandomico(); // Chama a função gerarRandomico e armazena o resultado
}

int* gerarRandomico() {
    static int r[10];
    int a;

    for (a = 0; a < 10; ++a) {
        r[a] = rand();
        printf("r[%d] = %d\n", a, r[a]);
    }
    return r; // Retorna o ponteiro para o array r
}
