#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

int main() {
    char nome[30];
    int i;

    printf("Digite o sobrenome do aluno(a): \n");
    fgets(nome, sizeof(nome), stdin);

    for (i = 0; nome[i] != ' ' && nome[i] != '\0'; i++) {
        nome[i] = toupper(nome[i]);
    }

    printf("\n\n Sobrenome convertido: %s\n\n", nome);
    return 0;
}
