#ESTRUTURA DE DADOS 
#Objetos do tipo sequência
#Ex.: Sequência de caracteres.
texto = "Aprendendo Python na diciplina de linguagem de programação"

print(f"Tamanho do texto = {len(texto)}")
print(f"Python in texto = {'Python' in texto}")
print(f"Quantidade de y no texto = {texto.count('y')}")
print(f"As 5 primeiras letras são: {texto[0:6]}")

vogais = ["a", "e", "i", "o","u"]
for vogal in vogais:
    print(f"Posição = {vogais.index(vogal)}, valor = {vogal}")

#FUNÇÃO SPLIT()
print(f"texto = {texto}")
print(f"Tamanho do texto = {len(texto)}\n")

palavras = texto.split()

print(f"Palavras = {palavras}")
print(f"Tamanho de palavras = {len(palavras)}")

#LISTA
linguagens = ["Python", "Java", "Javascript", "C", "C#", "Kotlin"]
print("Antes da listcomp = ", linguagens)

linguagens = [item.lower() for item in linguagens]
print("\nDepois da liscomp =", linguagens)

#FUNÇÕES MAP() E FILTER()
print("Exemplo")
linguagens ='''Python Java Javascript C C# Kotlin'''.split()
novaLista = map(lambda x: x.lower(), linguagens)
print(f"A nova lista é = {novaLista}\n")
novaLista = list(novaLista)
print(f"Agora sim, a nova lista é = {novaLista}")

#FUNÇÕES RANGE()
numeros = list(range(0,21))
numerosPares = list(filter(lambda x: x % 2 == 0, numeros))
print(numerosPares)

#TUPLAS
vogais = ("a", "e", "i", "o","u")
print(f"Tipo de objeto vogais = {type(vogais)}")

for p, x in enumerate(vogais):
    print(f"Posição = {p}, valor = {x}")