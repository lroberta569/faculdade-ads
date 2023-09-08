#include <stdio.h>
#include <stdlib.h> 

/* STRUCT */
struct automovel {
   char modelo[20];
   int ano;
   float valor;
};

/* LISTA LIGADA */
struct lista {
    int info;
    struct lista* prox;
};
typedef struct lista Lista;

struct alunos {
    char nome[25];
    struct alunos* prox;
};
typedef struct alunos Classe;

Lista* inicializa(void) {
    return NULL;
}

Lista* inserir(Lista* lista, int valor) {
    Lista* novo = (Lista*)malloc(sizeof(Lista));
    novo->info = valor;
    novo->prox = lista;
    return novo;
}

Lista* remover(Lista* l, int v){
    Lista* anterior = NULL;
    Lista* p = l;
    while(p!= NULL && p-> info!= v){
        anterior = p;
        p = p->prox;
    }

    if(p==NULL)
    return l;

    if(anterior == NULL){
        l=p->prox;
    }else{
        anterior-> prox = p->prox;

    }
    return l;
}

int main() {
    struct automovel dadosAutomovel;

    Lista* listaFinal;
    listaFinal = inicializa();
    listaFinal = inserir(listaFinal, 13);
    listaFinal = inserir(listaFinal, 56);

    return 0;
}

void imprimir(Lista* l){
    Lista* p;
    printf("Elementos:\n");
    for(p=l; p!=NULL;p=p->prox){
        printf("%d ->",p->info);
    }
}

Lista* buscar(Lista* l, int v){
    Lista* p;
    for(p = l; p!= NULL; p = p -> prox){
        if(p-> info ==v){
            return p;
        }
        return NULL;
    }
}

Lista* inserirPosicao(Lista* l, int pos, int v){
    int cont = 1;
    Lista* p = l;
    Lista* novo = (Lista*)malloc(sizeof(Lista));
    while(cont!= pos){
        p=p -> prox;
        cont++;
    }
}

/*PILHA*/
struct Pilha
{
    int topo;
    int capacidade;
    float* proxElem;
};
struct Pilha minhaPilha;

void criaPilha(struct Pilha *p, int c){
    p -> proxElem = (float*)malloc(c* sizeof(float));
    p -> topo -1;
    p -> capacidade = c;
}

void pushPilha(struct Pilha *p, float v){
    p -> topo++;
    p-> proxElem [p-> topo] =v;
}

void popPilha(struct Pilha *p){
    float aux = p-> proxElem[p -> topo];
    p-> topo --;
    return aux;
}

/*FILA*/
#define N 100

struct fila{
    int n;
    int ini;
    char vet[N];
};
typedef struct fila Fila;

Fila* iniciaFila(void){
    Fila* f = (Fila*) malloc(sizeof(Fila));
    f-> n = 0;
    f-> ini=0;
    return f;
}

void insereFila(Fila* f, char elem){
    int fim;
    if(f-> n == N){
        pringf("A fila está cheia.\n");
        exit(1);
    }

    fim = (f-> ini + f -> n) % N;
    f -> vet[fim] = elem;
    f-> n++;
}

float removeFila(Fila* f){
    char elem;
    if(filaVazia(f)){
        printf("A Fila esta vazia\n");
        exit(1);
    }
    elem = f -> vet[f -> ini];
    f-> ini = (f-> ini + 1) % N;
    f -> n--;
    return elem;
}

