# Importando bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importando os arquivos .csv
train = pd.read_csv('./datasets/train.csv', index_col=0)
test = pd.read_csv('./datasets/test.csv', index_col=0)

# Adquirindo informações sobre o número de linhas e colunas
train.isnull().sum()
test.isnull().sum()
print("Train Shape:",train.shape)
print("Test Shape:",test.shape)

# Pegando informações sobre o dataFrame
train.info()
test.info()

def analise_sobreviventes():
    sobrevivente = (train['Survived']==1).value_counts()
    return sobrevivente

print(f"Sobreviventes: ", analise_sobreviventes())