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
sex	        Sexo                      0 = mulher, 1 = homem
Age	        Idade em anos	
sibsp	    # Número de irmãos/cônjuges a bordo do Titanic	
parch	    # de pais/filhos a bordo do Titanic	
ticket	    Número do ticket	
fare	    Tarifa do passageiro	
cabin	    Número da cabine	
embarked	Porto que embarcou	      C = Cherbourg, Q = Queenstown, S = Southampton
Title       Titulo do passageiro      0 = , 1 = , 2 = , 3 = , 4 = , 5 = 
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

# Dicionario de titulos para o map que será feito posteriormente
DicionarioDeTitulos = {"Capt": "Officer","Col": "Officer","Major": "Officer","Jonkheer": "Royalty","Don": "Royalty","Sir" : "Royalty","Dr": "Officer","Rev": "Officer","the Countess":"Royalty","Mme": "Mrs","Mlle": "Miss","Ms": "Mrs","Mr" : "Mr","Mrs" : "Mrs","Miss" : "Miss","Master" : "Master","Lady" : "Royalty"}
# Função onde os titulos são criados. Os titulos são os apelidos que vem antes do nome
train['Title'] = train['Name'].map(lambda name:name.split(',')[1].split('.')[0].strip())
train['Title'] = train.Title.map(DicionarioDeTitulos)

# Limpando o Data Frame
df1=train.drop(['Name','Ticket','Cabin'], axis=1)

# Printando pós limpeza
print(df1.head())

# Convertendo strings para valores númericos
df1['Sex'] = df1['Sex'].map({'female':0, 'male':1})
df1['Embarked'] = df1['Embarked'].map({'S':0, 'C':1, 'Q':2,'nan':'NaN'})
df1['Title'] = df1['Title'].map({'Mr':0, 'Miss':1, 'Mrs':2,'Master':3,'Officer':4,'Royalty':5})

# Após verificar os nulos. Foi apresentado que tinham muitas idades nulas. Para isso foi feita a média das idades para cada sexo e fo colocado nesses valores nulos
# Variaveis para armazenar a idade média de cada sexo
idadeMediaHomem1 = df1[df1['Sex']==1]['Age'].median()
idadeMediaMulher1 = df1[df1['Sex']==0]['Age'].median()
# Atribui o valor de idade média aos passageiros que possuem a idade como nula
df1.loc[(df1.Age.isnull()) & (df1['Sex']==1),'Age'] = idadeMediaHomem1
df1.loc[(df1.Age.isnull()) & (df1['Sex']==0),'Age'] = idadeMediaMulher1

# Após mudar os valores dos nulos. Printei para verificar se tem algum valor nulo
tarifaMedia = df1['Fare'].median()
df1.loc[df1.Fare.isnull(), 'Fare'] = tarifaMedia

# Verificando qual é o titulo nulo. Após verificar que o titulo nulo se tratava de uma mulher que não estava acompanhada, dei um titulo adequado para ela
tituloNulo = df1[df1.Title.isnull()]
#print(tituloNulo)
df1 = df1.fillna(2)
