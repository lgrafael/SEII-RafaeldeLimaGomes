import pandas as pd
dados = pd.read_csv('~/code/SEII-RafaeldeLimaGomes/Semana03/Exercicio05/athlete_events.csv')

print(dados.head())

masculinos = dados.loc[dados['Sex'] =='M']

print(masculinos.head())