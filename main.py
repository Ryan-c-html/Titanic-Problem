# Importing libraries
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

#-------------------------------------------------------------------------------------------------------------
# Tabela de significado de cada variavel
#-------------------------------------------------------------------------------------------------------------
# Variavel	 Definição	              Chave

# Survived	 sobreviventes	          0 = Não, 1 = Sim
# pclass	 Classe do Ticket	      1 = 1st, 2 = 2nd, 3 = 3rd
# sex	     Sexo                     0 = mulher, 1 = homem
# Age	     Idade em anos	
# sibsp	     Número de irmãos/cônjuges a bordo do Titanic	
# parch	     Número de pais/filhos a bordo do Titanic	
# ticket	 Número do ticket	
# fare	     Tarifa do passageiro	
# cabin	     Número da cabine	
# embarked	 Porto que embarcou	      C = Cherbourg, Q = Queenstown, S = Southampton
# Title      Titulo do passageiro     0 = , 1 = , 2 = , 3 = , 4 = , 5 = 
#-------------------------------------------------------------------------------------------------------------
# Importando os arquivos .csv
train = pd.read_csv('./datasets/train.csv', index_col=0)
test = pd.read_csv('./datasets/test.csv', index_col=0)

# Analise das colunas do DataFrame
print(train.head())
print(test.head())
#-------------------------------------------------------------------------------------------------------------
# Limpando o Data Frame
df1=train.drop(['Name','Ticket','Cabin'], axis=1)
testData = test.drop(['Name', 'Ticket', 'Cabin'], axis=1)
#-------------------------------------------------------------------------------------------------------------
# Convertendo strings para valores numéricos
df1['Sex'] = df1['Sex'].map({'female':0, 'male':1})
df1['Embarked'] = df1['Embarked'].map({'S':0, 'C':1, 'Q':2,'nan':'NaN'})
testData['Sex'] = testData['Sex'].map({'female': 0, 'male': 1})
testData['Embarked'] = testData['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})
#-------------------------------------------------------------------------------------------------------------
# Variaveis para armazenar a idade média de cada sexo
idadeMediaHomem1 = df1[df1['Sex']==1]['Age'].median()
idadeMediaMulher1 = df1[df1['Sex']==0]['Age'].median()
# Atribui o valor de idade média aos passageiros que possuem a idade como nula
df1.loc[(df1.Age.isnull()) & (df1['Sex']==1),'Age'] = idadeMediaHomem1
df1.loc[(df1.Age.isnull()) & (df1['Sex']==0),'Age'] = idadeMediaMulher1
idadeMediaHomem = testData[testData['Sex'] == 1]['Age'].median()
idadeMediaMulher = testData[testData['Sex'] == 0]['Age'].median()
testData.loc[(testData.Age.isnull()) & (testData['Sex'] == 1), 'Age'] = idadeMediaHomem
testData.loc[(testData.Age.isnull()) & (testData['Sex'] == 0), 'Age'] = idadeMediaMulher
#-------------------------------------------------------------------------------------------------------------
# Função para verificar valores nulos no DataFrame
def verificaNulos(dataframe):
    valoresNulos = dataframe.isnull().sum()
    print('\n\nValores Nulos:\n', valoresNulos)
#-------------------------------------------------------------------------------------------------------------
# Verificando os nulos nas tabelas
#verificaNulos(df1)
#verificaNulos(testData)
#-------------------------------------------------------------------------------------------------------------
# 
tituloNulo = testData[testData.Embarked.isnull()]
print(EmbarkedNulo)
#df1 = df1.fillna(2)
#-------------------------------------------------------------------------------------------------------------
# Preenchendo valores nulos na tarifa com a mediana
tarifaMedia = testData['Fare'].median()
testData.loc[testData.Fare.isnull(), 'Fare'] = tarifaMedia





