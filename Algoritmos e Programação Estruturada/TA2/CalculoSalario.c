#include <stdio.h> 

int main(){
    float salario, inss, ir, salarioLiquido;

    printf("Digite seu salario bruto:");
    scanf("%f", &salario);

    if(salario <= 1693.72){
        inss = salario * 0.08f;
    } else if(salario >= 1693.73 && salario <= 2822.90){
        inss = salario * 0.09f;
    }else if(salario >= 2822.91 && salario <= 5646.80){
        inss = salario * 0.11f;
    }else{
        inss = 621.04f;
    }

    if(salario <= 1903.98){
        ir = 0;
    }else if(salario >= 1903.98 && salario <= 2826.65){
        ir = salario * 0.075f;
    }else if(salario >= 2826.65 && salario <= 3751.05){
        ir = salario * 0.15f;
    }else if(salario >= 23751.05 && salario <= 4664.68){
        ir = salario * 0.225f;
    }else{
        ir = salario * 0.275f;
    }

    salarioLiquido = salario - (inss + ir);

    printf("\n Desconto INSS: %f\n", inss);
    printf("\n Desconto IR: %f\n", ir);
    printf("\n Salario Liquido: %2.f\n",salarioLiquido);

    return 0;
}