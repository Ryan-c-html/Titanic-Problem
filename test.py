# Importando bibliotecas
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Importando os arquivos .csv
train = pd.read_csv('./datasets/train.csv', index_col=0)
test = pd.read_csv('./datasets/test.csv', index_col=0)

# Função para verificar valores nulos no DataFrame
def verificaNulos(dataframe):
    valoresNulos = dataframe.isnull().sum()
    print('\n\nValores Nulos:\n', valoresNulos)

# Dicionário de títulos para o mapeamento posterior
DicionarioDeTitulos = {"Capt": "Officer", "Col": "Officer", "Major": "Officer", "Jonkheer": "Royalty","Don": "Royalty", "Sir": "Royalty", "Dr": "Officer", "Rev": "Officer","the Countess": "Royalty", "Mme": "Mrs", "Mlle": "Miss", "Ms": "Mrs","Mr": "Mr", "Mrs": "Mrs", "Miss": "Miss", "Master": "Master", "Lady": "Royalty"}

# Função para criar os títulos (apelidos) a partir dos nomes
test['Title'] = test['Name'].map(lambda name: name.split(',')[1].split('.')[0].strip())
test['Title'] = test['Title'].map(DicionarioDeTitulos)


# Limpando o DataFrame
testData = test.drop(['Name', 'Ticket', 'Cabin'], axis=1)


# Convertendo strings para valores numéricos
testData['Sex'] = testData['Sex'].map({'female': 0, 'male': 1})
testData['Embarked'] = testData['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})




testData = pd.get_dummies(testData, columns=['Title'], prefix='Title')


# Função para verificar os números nulos na tabela
# verificaNulos(testData)

# Preenchendo valores nulos na idade com a média por sexo
idadeMediaHomem = testData[testData['Sex'] == 1]['Age'].median()
idadeMediaMulher = testData[testData['Sex'] == 0]['Age'].median()
testData.loc[(testData.Age.isnull()) & (testData['Sex'] == 1), 'Age'] = idadeMediaHomem
testData.loc[(testData.Age.isnull()) & (testData['Sex'] == 0), 'Age'] = idadeMediaMulher

# Preenchendo valores nulos na tarifa com a mediana
tarifaMedia = testData['Fare'].median()
testData.loc[testData.Fare.isnull(), 'Fare'] = tarifaMedia

# Verificando e tratando o título nulo
tituloNulo = testData[testData['Title'].isnull()]
# print(tituloNulo)
testData = testData.fillna(2)

# Adicionando a coluna "Survived"
testData['Survived'] = 0

# Imprimindo as primeiras linhas do DataFrame
print(testData.head())

# Verificando se a coluna 'Survived' está presente no conjunto de treinamento
if 'Survived' in train.columns:
    # Extrair a variável de destino do conjunto de treinamento
    y_train = train['Survived']
else:
    print("A coluna 'Survived' não está presente no conjunto de treinamento.")

# Verificando se a coluna 'Survived' está presente no conjunto de teste
if 'Survived' in testData.columns:
    # Extrair a variável de destino do conjunto de teste
    y_test = testData['Survived']
else:
    print("A coluna 'Survived' não está presente no conjunto de teste.")

# Dividindo os dados em conjuntos de treinamento e teste
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
print(f'\n\nAcurácia do modelo: {accuracy * 100:.2f}%')

# Agora, se você quiser fazer previsões para novos dados (por exemplo, os dados de teste originais), você pode fazer algo assim:
testData_sem_target = testData.drop('Survived', axis=1)
novas_previsoes = model.predict(testData_sem_target)





