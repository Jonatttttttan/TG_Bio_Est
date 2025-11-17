import pandas as pd
import numpy as np

caminho = "C:\\Users\\Pc\\Desktop\\Organizacao_Meus_Docs\\Univap\\Ciencias_Biologicas\\TG1\\dados_epidemiologicos_formatados.xlsx"

dicionario_base = {"semana" : [], "temp_maxima" : [], "temp_media" : [], "temp_minima" : [], "umd_maxima" : [], "umd_media" : [], "umd_minima" : [], "qtd_casos" : []}

pf = pd.read_excel(caminho)

dicionario_base["semana"] = pf["data_iniSE"]
dicionario_base["temp_maxima"] = pf["tempmax"]
dicionario_base["temp_media"] = pf["tempmed"]
dicionario_base["temp_minima"] = pf["tempmin"]
dicionario_base["umd_maxima"] = pf["umidmax"]
dicionario_base["umd_minima"] = pf["umidmin"]
dicionario_base["umd_media"] = pf["umidmed"]
dicionario_base["qtd_casos"] = pf["casos"]

df2 = pd.DataFrame(dicionario_base)
with pd.ExcelWriter(caminho, mode="a", engine="openpyxl", if_sheet_exists="replace") as writer:
    df2.to_excel(writer, sheet_name="CasosXClima", index=False)







