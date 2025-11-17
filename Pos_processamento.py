import pandas as pd
import numpy as np

from Xip.T1 import caminho

caminho = "C:\\Users\\Pc\\Desktop\\Organizacao_Meus_Docs\\Univap\\Ciencias_Biologicas\\TG1\\dados_epidemiologicos_formatados.xlsx"

pf = pd.read_excel(caminho, sheet_name="CasosXClima")
cabecario = pf.columns

lista_indice_max = list(filter(lambda x: int(pf["qtd_casos"][x] > 1000), [y for y in range(0, len(pf))]))
lista_indice_min = list(filter(lambda x: int(pf["qtd_casos"][x] <= 1000), [y for y in range(0, len(pf))]))

dic_filtrado_max = { x : [pf[x][y] for y in lista_indice_max ] for x in cabecario}
dic_filtrado_min = { x : [pf[x][y] for y in lista_indice_min ] for x in cabecario}

print(dic_filtrado_max["temp_maxima"])

df2 = pd.DataFrame(dic_filtrado_max)
df3 = pd.DataFrame(dic_filtrado_min)

with pd.ExcelWriter(caminho, mode="a", engine="openpyxl", if_sheet_exists="replace") as writer:
    df2.to_excel(writer, sheet_name="Casos_Mil", index=False)

with pd.ExcelWriter(caminho, mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
    df3.to_excel(writer, sheet_name="Poucos_Casos", index=False)



