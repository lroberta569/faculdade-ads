#ALGORITMOS DE BUSCA
nomes = "João Marcela Sonia Sandra Roberto Gabriel".split()
print("Marcela" in nomes)
print("José" in nomes)

#BUSCA LINEAR (OU BUSCA SEQUENCIAL)
def executarBuscaLinear(lista, valor):
    for elemento in lista:
        if valor == elemento:
            return True
        return False

#FUNÇÃO INDEX()
vogais = "aeiou"
resultado = vogais.index("e")
print(resultado)

#BUSCA BINÁRIA
def executarBuscaBinaria(lista, valor):
    minimo = 0
    maximo = len(lista) - 1

    while minimo <= maximo:
        #Encontra o elemento e divide a lista ao meio
        meio = (minimo + maximo) // 2
        #Verifica se o valor procurado está a esquerda ou a direita do valor cental
        if valor < lista[meio]:
            maximo = meio - 1
        elif valor < lista[meio]:
            minimo = meio +1
        else:
            return True #Se o valor for encontrado para aqui
        
        return False #Se chegar até aqui, significa que o valor não foi encontrado
