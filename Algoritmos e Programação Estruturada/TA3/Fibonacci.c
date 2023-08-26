#include <stdio.h>

int main() {
    int n, i;
    long long int a = 0, b = 1, next;

    printf("Quantos termos da sequencia de Fibonacci voce deseja gerar? ");
    scanf("%d", &n);

    printf("Os primeiros %d termos da sequencia de Fibonacci sao:\n", n);

    for (i = 1; i <= n; ++i) {
        if (i == 1) {
            printf("%lld", a);
        } else if (i == 2) {
            printf(", %lld", b);
        } else {
            next = a + b;
            printf(", %lld", next);
            a = b;
            b = next;
        }
    }
    printf("\n");

    return 0;
}
