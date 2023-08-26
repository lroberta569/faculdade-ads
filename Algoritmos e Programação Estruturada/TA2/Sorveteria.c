#include <stdio.h> 

int main(){
    int i;

    do{
        printf("\n Digite um numero do sabor \n");
        printf("\t 1 - Baunilha \n");
        printf("\t 2 - Chocolate \n");
        printf("\t 3 - Morango \n");
        printf("\t 4 - Menta \n");

        scanf("%d",&i);
    }while((i < 1 ) || (i > 4));

    switch (i) {
    case 1:
        printf("\t\t Voce escolheu Baunilha \n");
        printf("\t\t Informacoes nutricionais: \n");
        printf("\t\n Calorias: 137 kcal \n Gordura: 7g \n Carboidratos: 17g \n Acucares: 16g \n Proteina: 2g\n");
        break;
    case 2:
        printf("\t\t Voce escolheu Chocolate \n");
        printf("\t\t Informacoes nutricionais: \n");
        printf("\t\n Calorias: 143 kcal \n Gordura: 7g \n Carboidratos: 19g \n Acucares: 17g \n Proteina: 2g\n");
        break;
    case 3:
        printf("\t\t Voce escolheu Morango \n");
        printf("\t\t Informacoes nutricionais: \n");
        printf("\t\n Calorias: 106 kcal \n Gordura: 5g \n Carboidratos: 14g \n Acucares: 13g \n Proteina: 2g\n");
        break;
    case 4:
        printf("\t\t Voce escolheu Menta \n");
        printf("\t\t Informacoes nutricionais: \n");
        printf("\t\n Calorias: 116 kcal \n Gordura: 6g \n Carboidratos: 15g \n Acucares: 13g \n Proteina: 1g\n");
        break;
    default:
        break;
}

    return 0;
}