/*Foi solicitado a você automa9zar o cálculo de uma
reação chamada de proteção. Nessa reação, um
composto A, de massa 321,43 g/mol será somando
a um composto B de massa 150,72 g/mol. Seu
programa, além de calcular o composto com base
nas informações do usuário, deverá também exibir
os valores de referência das combinações: (1,2 :
1,0), (1,4 : 1,0) e (1,0 : 1,6).*/
#include <stdio.h>

float calcularMassa(float a, float b){
    const float mA = 321.43;
    const float mB = 150.72;

    printf("\n 1,2 : 1,0 \t: =%f", (1.2*mA+1*mB));
    printf("\n 1.4 : 1.0 \t: =%f", (1.4*mA+1*mB));
    printf("\n 1.0 : 1.6 \t: =%f", (1.0*mA+1.6*mB));

    return(a * mA) + (b*mB);
}
int main() {
    float a=0, b=0, resultado=0;
    
    printf("\n Digite as massas do elemento A e B:");
    scanf("%f %f", &a,&b);

    resultado = calcularMassa(a,b);
    printf("\n Resultado %f", resultado);
    return 0;
}
