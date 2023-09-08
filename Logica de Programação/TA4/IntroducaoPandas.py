import pandas as pd

#INTRODUÇÃO A BIBLIOTECA PANDAS
pd.Series(data=5)

listaNomes = "Larissa Gabriel Sandra Roberto Regina".split()

pd.Series(listaNomes) #Cria uma Series com o valor da listaNomes

dados = {
    'nome1': 'Larissa',
    'nome2': 'Gabriel',
    'nome3': 'Sandra',
    'nome4': 'Roberto',
    'nome5': 'Regina',
}

pd.Series(dados) #Cria uma Series com um dicionário

seriesDados = pd.Series([10.2, -1, None, 15, 24.4]) 
print("Quantidade de linhas =", seriesDados.shape) #Retorna uma tupla com o números de linhas
print("Tipos de dados =", seriesDados.dtypes) #Retorna o tipo de dados, se for misto sera object
print("Valores são únicos?", seriesDados.is_unique) #Verifica se os valores são únicos (sem duplicações)
print("Existem valores nulos?", seriesDados.hasnans) #Verifica se existem valores nulos
print("Quantos valores existem?", seriesDados.count()) #Conta quantos valores existem (excluí os nulos)
print("Qual o menor valor", seriesDados.min()) #Extrai o menor valor da Series (nesse caso os dados precisam ser do mesmo tipo)
print("Qual o maior valor?", seriesDados.max()) #Extrai o valor máximo, com a mesma condição do mínimo
print("Qual é a média aritmética?", seriesDados.mean()) #Extrai a média aritmética de uma Series numérica
print("Qual o desvio padrão?", seriesDados.std()) #Extrai o desvio padrão de uma Series numérica
print("Qual a mediana?", seriesDados.median()) #Extrai a mediana de uma Series numérica
print("\nResumo:\n", seriesDados.describe()) #Extrai um resumo sobre os dados na Series

#CONSTRUTOR DATAFRAME COM LISTA
pd.DataFrame(listaNomes, columns=['nome'])
print(pd.DataFrame(listaNomes, columns=['nome']))

#MANIPULAÇÃO DE DADOS EM PANDAS (LEITURA DE JSON E CSV COM PANDAS)
url = 'https://pt.wikipedia.org/wiki/Brasil'

dfs = pd.read_html(url)
print(type(dfs))
print(len(dfs))

