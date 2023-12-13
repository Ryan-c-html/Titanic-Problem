# Importando bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Importando os arquivos .csv
train = pd.read_csv('./datasets/train.csv', index_col=0)
test = pd.read_csv('./datasets/test.csv', index_col=0)

# Analisando informações
print(train.head())

# Analisando o número de linhas e colunas
print("\n\nNúmero de colunas e linhas")
print(train.shape)

# Analisando o número de homens e mulheres
print("\n\nNúmero de Homens e mulheres")
print(train['Sex'].value_counts())

# Analisando o número de pessoas em cada classe
print("\n\nNúmero de pessoas em cada classe")
print(train['Pclass'].value_counts())

# Limpando o dataFrame
df1=train.drop(['Name','Ticket','Cabin'], axis=1)

# Printando pós limpeza
print(df1.head())

# Convertendo strings para valores númericos
df1['Sex']=df1['Sex'].map({'female':0, 'male':1})
df1['Embarked']=df1['Embarked'].map({'S':0, 'C':1, 'Q':2,'nan':'NaN'})

# Printando pós redefinição
print(df1.head())

# Variaveis para armazenar a idade média de cada sexo
idadeMediaHomen = df1[df1['Sex']==1]['Age'].median()
idadeMediaMulher = df1[df1['Sex']==0]['Age'].median()