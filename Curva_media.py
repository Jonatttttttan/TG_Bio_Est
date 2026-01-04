import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.impute import SimpleImputer

caminho = "C:\\Users\\Pc\\Desktop\\Organizacao_Meus_Docs\\Univap\\Ciencias_Biologicas\\TG1\\Base_de_dados\\dengue_2-50.csv"
X = pd.read_csv(caminho, delimiter=",")
df = X.loc[:,["SE", "casos"]]
anos = [str(x) for x in range(2010, 2026)]
df["semana"] = list(map(lambda x: str(x)[4:], df["SE"]))
df["SE"] = list(map(lambda x: str(x)[:4], df["SE"]))
print(df.head())
dic = {x : df[df["SE"] == x] for x in anos}
qtd = [len(dic[x]) for x in anos]

X2 = [x for x in range(51, -1, -1)]
print(X2)
df2 = {x : [list(dic[y]["casos"])[x] if len(dic[y]) > x else np.nan for y in anos] for x in X2}
imputer = SimpleImputer(strategy="mean")
print(df2)
'''
col = np.array(df2[51]).reshape(-1, 1)
df2[51] = imputer.fit_transform(col).ravel().tolist()
print(df2[51])'''

df2 = {x : sum(imputer.fit_transform(np.array(df2[x]).reshape(-1,1)).ravel().tolist()) // len(df2[x]) for x in X2}
print(df2)
novas_chaves = [51 - x + 1 for x in X2]
print(novas_chaves)
df3 = {x : df2[51 - x + 1] for x in novas_chaves}
print(df3.values())

# Plotagem do gráfico
X = list(df3.keys())
y = list(df3.values())
figura = plt.figure(figsize=(12, 8))

