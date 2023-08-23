#Estruturas de repetição: While
numero = 1

while numero != 0:
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        print("Número par!")
    else:
        print("Número ímpar!")

#Estruturas de repetição: For
nome = "Guido"

for c in nome:
    print(c)

for i, c in enumerate(nome):
    print(f"Posição = {i}, valor = {c}")

#Controle de repetição com range, break e continue
#Exemplo usando range()
for x in range(5):
    print(x)

#Exemplo usando break
disciplina = "Linguagem de Programação"

for c in disciplina:
    if c == "a":
        break
    else:
        print(c)

#Exemplo usando continue
disciplina = "Linguagem de Programação"

for c in disciplina:
    if c == "a":
        continue
    else:
        print(c)
