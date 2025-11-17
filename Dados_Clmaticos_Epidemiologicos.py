import pandas as pd
import numpy as np
import csv

caminho = "C:\\Users\\Pc\\Desktop\\Organizacao_Meus_Docs\\Univap\\Ciencias_Biologicas\\TG1\\dengue_52-36.csv"

'''with open(caminho, mode='r', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo, delimiter=',')
    for linha in leitor:
        print(linha) # cada linha vira uma lista'''

df = pd.read_csv(caminho)

print(df.columns)
print(type(df))

df.to_excel("C:\\Users\\Pc\\Desktop\\Organizacao_Meus_Docs\\Univap\\Ciencias_Biologicas\\TG1\\dados_epidemiologicos_formatados.xlsx", sheet_name="Epidemiologia_dengue_2023-2025", index=False)




