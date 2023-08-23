# Estrutura Condicional Simples
nome = "Daniel"
sobrenome = ""
lista = []

if nome:
    print("A variável nome não é vazia")


# Estrutura Condicional Composta
valor1 = 10
valor2 = 20

if valor1 > valor2:
    print("O valor1 é maior que o valor2")
else:
    print("O valor2 é maior que o valor1")

# Estrutura Encadeada
cor = "amarelo"

if cor == "verde":
    print("Acelerar")
elif cor == "amarelo":
    print("Atenção")
else:
    print("Parar")

'''Estrutura condicional usando os operadores booleanos
Um aluno só pode ser aprovado caso ele tenha menos de 5 faltas e média final igual ou superior a 7.'''
quantidadeFaltas = int(input("Digite a quantidade de faltas: "))
mediaFinal = float(input("Digite a média final: "))

if quantidadeFaltas <= 5 and mediaFinal >= 7:
    print("Aluno aprovado!")
else:
    print("Aluno repovado!")
