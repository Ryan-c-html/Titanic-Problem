# Importando bibliotecas
import pandas as pd
import numpy as np

# Importando os arquivos .csv
train = pd.read_csv('./datasets/train.csv', index_col=0)
test = pd.read_csv('./datasets/test.csv', index_col=0)

# Primeiro print para avaliar a tabela
print(test.head())

# Funções do código
    # Verificando quantos valores nulos o Data Frame possui
def verificaNulos():
    valoresNulos = testData.isnull().sum()
    print('\n\n')
    print(valoresNulos)

DicionarioDeTitulos = {"Capt": "Officer","Col": "Officer","Major": "Officer","Jonkheer": "Royalty","Don": "Royalty","Sir" : "Royalty","Dr": "Officer","Rev": "Officer","the Countess":"Royalty","Mme": "Mrs","Mlle": "Miss","Ms": "Mrs","Mr" : "Mr","Mrs" : "Mrs","Miss" : "Miss","Master" : "Master","Lady" : "Royalty"}

# Limpando o Data Frame
testData = test.drop(['Name','Ticket','Cabin'], axis=1)
print(testData.head())

# Convertendo strings para valores númericos
testData['Sex'] = testData['Sex'].map({'female':0, 'male':1})
testData['Embarked'] = testData['Embarked'].map({'S':0, 'C':1, 'Q':2,'nan':'NaN'})
print(testData.head())

# Variaveis para armazenar a idade média de cada sexo
idadeMediaHomem = testData[testData['Sex']==1]['Age'].median()
idadeMediaMulher = testData[testData['Sex']==0]['Age'].median()
# Atribui o valor de idade média aos passageiros que possuem a idade como nula
testData.loc[(testData.Age.isnull()) & (testData['Sex']==0),'Age'] = idadeMediaHomem
testData.loc[(testData.Age.isnull()) & (testData['Sex']==1),'Age'] = idadeMediaMulher
print(testData.head())

#verificaNulos()

# Após mudar os valores dos nulos. Printei para verificar se tem algum valor nulo
tarifaMedia = testData['Fare'].median()
testData.loc[testData.Fare.isnull(), 'Fare'] = tarifaMedia

#verificaNulos()









