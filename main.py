import pandas as pd

df = pd.read_csv('./datasets/train.csv', index_col=0)

print(df)