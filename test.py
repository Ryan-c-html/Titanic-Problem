# Importando bibliotecas
import pandas as pd
#from sklearn.ensemble import RandomForestClassifier
#from sklearn.model_selection import train_test_split
#from sklearn.metrics import accuracy_score


# Importando os arquivos .csv
train = pd.read_csv('./datasets/train.csv', index_col=0)
test = pd.read_csv('./datasets/test.csv', index_col=0)

# Funções do código
    # Verificando quantos valores nulos o Data Frame possui
def verificaNulos():
    valoresNulos = testData.isnull().sum()
    print('\n\n')
    print(valoresNulos)

# Primeiro print para avaliar a tabela
print(test.head())

# Dicionario de titulos para o map que será feito posteriormente
DicionarioDeTitulos = {"Capt": "Officer","Col": "Officer","Major": "Officer","Jonkheer": "Royalty","Don": "Royalty","Sir" : "Royalty","Dr": "Officer","Rev": "Officer","the Countess":"Royalty","Mme": "Mrs","Mlle": "Miss","Ms": "Mrs","Mr" : "Mr","Mrs" : "Mrs","Miss" : "Miss","Master" : "Master","Lady" : "Royalty"}
# Função onde os titulos são criados. Os titulos são os apelidos que vem antes do nome
test['Title'] = test['Name'].map(lambda name:name.split(',')[1].split('.')[0].strip())
test['Title'] = test.Title.map(DicionarioDeTitulos)

# Limpando o Data Frame
testData = test.drop(['Name','Ticket','Cabin'], axis=1)
#print(testData.head())

# Convertendo strings para valores númericos
testData['Sex'] = testData['Sex'].map({'female':0, 'male':1})
testData['Embarked'] = testData['Embarked'].map({'S':0, 'C':1, 'Q':2,'nan':'NaN'})
testData['Title'] = testData['Title'].map({'Mr':0, 'Miss':1, 'Mrs':2,'Master':3,'Officer':4,'Royalty':5})
#print(testData.head())

# Função que verifica os numeros nulos na tabela
#verificaNulos()

# Após verificar os nulos. Foi apresentado que tinham muitas idades nulas. Para isso foi feita a média das idades para cada sexo e fo colocado nesses valores nulos
# Variaveis para armazenar a idade média de cada sexo
idadeMediaHomem1 = testData[testData['Sex']==1]['Age'].median()
idadeMediaMulher1 = testData[testData['Sex']==0]['Age'].median()
# Atribui o valor de idade média aos passageiros que possuem a idade como nula
testData.loc[(testData.Age.isnull()) & (testData['Sex']==1),'Age'] = idadeMediaHomem1
testData.loc[(testData.Age.isnull()) & (testData['Sex']==0),'Age'] = idadeMediaMulher1
#print(testData.head())

# Após mudar os valores dos nulos. Printei para verificar se tem algum valor nulo
tarifaMedia = testData['Fare'].median()
testData.loc[testData.Fare.isnull(), 'Fare'] = tarifaMedia
#verificaNulos()

# Verificando qual é o titulo nulo. Após verificar que o titulo nulo se tratava de uma mulher que não estava acompanhada, dei um titulo adequado para ela
tituloNulo = testData[testData.Title.isnull()]
#print(tituloNulo)
testData = testData.fillna(2)
#verificaNulos()

print(testData.head())

'''
if 'Survived' in train.columns:
    # Extrair variável de destino do conjunto de treinamento
    y_train = train['Survived']
else:
    print("A coluna 'Survived' não está presente no conjunto de treinamento.")

# Certifique-se de que a coluna "Survived" está presente no conjunto de teste
if 'Survived' in testData.columns:
    # Extrair variável de destino do conjunto de teste
    y_test = testData['Survived']
else:
    print("A coluna 'Survived' não está presente no conjunto de teste.")


X = testData.drop('Survived', axis=1)
y = testData['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializando o modelo
model = RandomForestClassifier(random_state=42)

# Treinando o modelo
model.fit(X_train, y_train)

# Fazendo previsões no conjunto de teste
predictions = model.predict(X_test)

# Avaliando a precisão do modelo
accuracy = accuracy_score(y_test, predictions)
print(f'Acurácia do modelo: {accuracy * 100:.2f}%')

# Agora, se você quiser fazer previsões para novos dados (por exemplo, os dados de teste originais), você pode fazer algo assim:
testData_sem_target = testData.drop('Survived', axis=1)
novas_previsoes = model.predict(testData_sem_target)
'''




