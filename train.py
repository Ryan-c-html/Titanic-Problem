# Importando bibliotecas
import pandas as pd
import numpy as np

# Importando os arquivos .csv
train = pd.read_csv('./datasets/train.csv', index_col=0)
test = pd.read_csv('./datasets/test.csv', index_col=0)

''' Tabela do que cada coisa significa
Variavel	Definição	              Chave

Survived	sobreviventes	          0 = Não, 1 = Sim
pclass	    Classe do Ticket	      1 = 1st, 2 = 2nd, 3 = 3rd
sex	        Sexo
Age	        Idade em anos	
sibsp	    # Número de irmãos/cônjuges a bordo do Titanic	
parch	    # de pais/filhos a bordo do Titanic	
ticket	    Número do ticket	
fare	    Tarifa do passageiro	
cabin	    Número da cabine	
embarked	Porto que embarcou	      C = Cherbourg, Q = Queenstown, S = Southampton
'''

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

# Limpando o Data Frame
df1=train.drop(['Name','Ticket','Cabin'], axis=1)

# Printando pós limpeza
print(df1.head())

# Convertendo strings para valores númericos
df1['Sex'] = df1['Sex'].map({'female':0, 'male':1})
df1['Embarked'] = df1['Embarked'].map({'S':0, 'C':1, 'Q':2,'nan':'NaN'})

# Printando pós redefinição
print(df1.head())

# Variaveis para armazenar a idade média de cada sexo
idadeMediaHomem = df1[df1['Sex']==1]['Age'].median()
idadeMediaMulher = df1[df1['Sex']==0]['Age'].median()

# Atribui o valor de idade média aos passageiros que possuem a idade como nula
df1.loc[(df1.Age.isnull()) & (df1['Sex']==0),'Age'] = idadeMediaHomem
df1.loc[(df1.Age.isnull()) & (df1['Sex']==1),'Age'] = idadeMediaMulher

print(df1.head())

# Verificando quantos valores nulos o Data Frame possui
valoresNulos = df1.isnull().sum()
print("\n\n")
print(valoresNulos) 

# Após descobrir que tem duas linhas na coluna "Embarked" que estão nulas. Printei para avaliar
embarkedNulos = df1[df1.Embarked.isnull()]
# print(embarkedNulos)
df1 = df1.fillna(1)

# Verificando novamente se o Data Frame possui algum valor nulo
valoresNulos = df1.isnull().sum()
print("\n\n")
print(valoresNulos)

