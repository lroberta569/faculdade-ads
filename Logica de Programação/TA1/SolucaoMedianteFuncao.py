#Função definida pelo usuário
def imprimirMensagem(disciplina, curso):
    print(f"Minha primeira função em Python desenvolvida na disciplina: {disciplina}, do curso: {curso}.")

imprimirMensagem("Python", "ADS")

#Funções com parâmetros definidos e indefinidos
'''1. Parâmetro posicional, obrigatório, sem valor default (padrão), 
tentar invocar a função, sem passar os parâmetros, acarreta um 
erro.'''
def somar(a, b):
    return a + b

r = somar(2,3)
print(r)

'''2. Parâmetro posicional, obrigatório, com valor default (padrão), 
quando a função for invocada, caso nenhum valor seja passado, o 
valor default é utilizado.'''
def calcularDesconto(valor, desconto=0):
    #O parâmetro desconto possui valor zero default
    valorComDesconto = valor - (valor * desconto)
    return valorComDesconto

valor1 = calcularDesconto(100) #Não aplica nenhum desconto
valor2 = calcularDesconto(100, 0.25) #Aplica desconto de 25%

print(f"\nPrimeiro valor a ser pago = {valor1}")
print(f"\nSegundo valor a ser pago = {valor2}")

'''3. Parâmetro nominal, obrigatório, sem valor default (padrão). Não 
mais importa a posição dos parâmetros, pois eles serão identificados 
pelo nome, a chamada da função é obrigatório passar todos os 
valores e sem valor default.'''
def converterMaiuscula(texto, flagMaiuscula):
    if flagMaiuscula:
        return texto.upper()
    else:
        return texto.lower()
texto = converterMaiuscula(flagMaiuscula=True, texto="João") #Passagem nominal de parâmetros
print(texto)

'''4. Parâmetro nominal, obrigatório, com valor default (padrão), nesse 
grupo os parâmetros podem possuir valor default.'''
def converterMaiuscula(texto, flagMaiuscula=True):
    if flagMaiuscula:
        return texto.upper()
    else:
        return texto.lower()
texto1 = converterMaiuscula(flagMaiuscula=True, texto="LINGUAGEM de programação")
texto2 = converterMaiuscula(flagMaiuscula=True, texto="LINGUAGEM de programação")  
print(f"\nTexto 1 = {texto1}")
print(f"\nTexto 2 = {texto2}")

'''5. Parâmetro posicional e não obrigatório (args), a passagem de
valores é feita de modo posicional, porém a quantidade não é
conhecida'''
def imprimirParametros(*args):
    quantidadeParametros = len(args)
    print(f"Quantidade de parâmetros = {quantidadeParametros}")

    for i, valor in enumerate(args):
        print(f"Posição = {i}, valor = {valor}")

print("\nChamada 1")
imprimirParametros("São Paulo", 10, 23.78, "João")
print("\nChamada 2")
imprimirParametros(10, "São Paulo")

'''6. Parâmetro nominal e não obrigatório (kwargs), agora a
passagem é feita de modo nominal e não posicional, o que nos 
permite acessar tanto o valor do parâmetro quanto o nome da 
variável que o armazena.'''
def imprimirParametros(**kwargs):
    print(f"Tipo de objeto recebido = {type(kwargs)}\n")
    quantidadeParametros = len(kwargs)
    print(f"Quantidade de parâmetros = {quantidadeParametros}")

    for chave, valor in kwargs.items():
        print(f"Variável = {chave}, valor = {valor}")

print("\nChamada 1")
imprimirParametros(cidade ="São Paulo", idade=10, nome="João")
print("\nChamada 2")
imprimirParametros(desconto=10, valor=100)

