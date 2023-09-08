import pandas as pd
from datetime import date
from datetime import datetime as dt

#TRABALHANDO COM DADOS (CRIAR NOVAS COLUNAS)
'''EX: Uma coluna que adiciona a data de extração das infromações'''
listaNomes = "Larissa Gabriel Sandra Roberto Regina".split()

pd.Series(listaNomes) #Cria uma Series com o valor da listaNomes


dfs = pd.DataFrame(listaNomes, columns=['nome'])
print(pd.DataFrame(listaNomes, columns=['nome']))

dataExtracao = dt.now()
dfs['dataExtracao'] = dataExtracao
'''O formato resultante ano-mês-dia é um padrão do datetime64[ns], que segue o padrão internacional'''
dfs['dataExtracao'] = dfs['dataExtracao'].astype('datetime64[ns]')
dfs = dfs.append({'nome': 'TESTE', 'dataExtracao': dt(2020, 5, 17)}, ignore_index=True)

dfs.sort_values(by='dataExtracao', ascending=False, inplace=True)

print(dfs)
print(dfs.info())
print(dfs.head())
