#FUNÇÃO SORTED() E SORT()
lista = [10, 4, 1, 15, -3]
listaOrdenada1 = sorted(lista)

listaOrdenada2 = lista.sort()

print("Lista = ", lista, "\n")

print("Lista Ordenada 1 = ", listaOrdenada1)
print("Lista Ordenada 2 = ", listaOrdenada2)

print("Lista = ", lista)

##########################################################

lista2 = [7, 4]

if lista2[0] > lista2[1]:
    aux = lista2[1]
    lista2[1] = lista2[0]
    lista2[0] = aux

print(lista2)

###########################################################
lista3 = [5, -1]

if lista3[0] > lista3[1]:
    lista3[0], lista3[1] = lista3[1], lista3[0]

print(lista3)

############################################################
#SELECTION SORT (ORDENAÇÃO POR SELEÇÃO)
def executarSelectionSort(lista):
    n = len(lista)
    for i in range(0, n):
        indexMenor = i
        for j in range(i+1, n):
            if lista[j] < lista[indexMenor]:
                indexMenor = j
            lista[i], lista[indexMenor] = lista[indexMenor], lista[i]
    return lista

lista4 = [10, 9, 5, 8, 11, 3]
print(executarSelectionSort(lista4))

#BUBBLE SORT
def executarBubbleSort(lista):
    n = len(lista)
    for i in range(n-1):
        for j in range(n-1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
        return lista

lista5 = [10, 9, 5, 8, 11, -1, 3]
print(executarBubbleSort(lista5))

