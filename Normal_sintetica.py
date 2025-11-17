#from curses.ascii import alt

import pandas as pd
import numpy as np
import statistics
from sklearn.impute import SimpleImputer

from numpy.distutils.system_info import dfftw_info

str_caminho_Campos_do_Jordao = "C:\\Users\\Pc\\Desktop\\Organizacao_Meus_Docs\\Univap\\Ciencias_Biologicas\\TG1\\Dados_CPJ.xlsx"
str_caminho_Sao_Luis_do_Paraitinga = "C:\\Users\\Pc\\Desktop\\Organizacao_Meus_Docs\\Univap\\Ciencias_Biologicas\\TG1\\Dados_Spt.xlsx"
str_caminho_Taubate = "C:\\Users\\Pc\\Desktop\\Organizacao_Meus_Docs\\Univap\\Ciencias_Biologicas\\TG1\\Dados_Tbt.xlsx"

# Altitudes
alt_SJC = 646
alt_CJ = 1628
alt_SPT = 770
alt_Tbt = 580

# Distâncias
dTbt = 15000
dCJ = 60000
dSPT = 45000

# Pesos
wTbt = 0.7849
wCJ = 0.1127
wSPT = 0.1023



imputer = SimpleImputer(strategy="median")
dfCJ = pd.read_excel(str_caminho_Campos_do_Jordao, sheet_name="Plan1")
dfSLP = pd.read_excel(str_caminho_Sao_Luis_do_Paraitinga, sheet_name="Plan1")
dfTbt = pd.read_excel(str_caminho_Taubate, sheet_name="Plan1")

# Capturando Dados
lst_Dados_Precipitacao_Tbt = [str(list(dfTbt["PRECIPITACAO TOTAL, MENSAL (AUT)(mm)"])[x]) + "-" + str(list(dfTbt["Data Medicao"])[x]).split("-")[1] for x in range(0, len(list(dfTbt["PRECIPITACAO TOTAL, MENSAL (AUT)(mm)"])))]
lst_Dados_Precipitacao_CJ = [str(list(dfTbt["PRECIPITACAO TOTAL, MENSAL (AUT)(mm)"])[x]) + "-" + str(list(dfTbt["Data Medicao"])[x]).split("-")[1] for x in range(0, len(list(dfTbt["PRECIPITACAO TOTAL, MENSAL (AUT)(mm)"])))]
lst_Dados_Precipitacao_SLP = [str(list(dfTbt["PRECIPITACAO TOTAL, MENSAL (AUT)(mm)"])[x]) + "-" + str(list(dfTbt["Data Medicao"])[x]).split("-")[1] for x in range(0, len(list(dfTbt["PRECIPITACAO TOTAL, MENSAL (AUT)(mm)"])))]

# Processa dados faltantes
lstPrecipitacao_Tbt_Completo = [[list(imputer.fit_transform(pd.DataFrame([float(x.split("-")[0]) for x in lst_Dados_Precipitacao_Tbt])))[12*u + v] for v in range(0, 12)] for u in range (0, 5)]
print("media precipitação corrigida", lstPrecipitacao_Tbt_Completo[1])
lstPrecipitacao_CJ_Completo = [[list(imputer.fit_transform(pd.DataFrame([float(x.split("-")[0]) for x in lst_Dados_Precipitacao_CJ])))[12*u + v] for v in range(0, 12)] for u in range (0, 5)]
lstPrecipitacao_SLP_Completo = [[list(imputer.fit_transform(pd.DataFrame([float(x.split("-")[0]) for x in lst_Dados_Precipitacao_SLP])))[12*u + v] for v in range(0, 12)] for u in range (0, 5)]
lista_precipitacao_completa=[lstPrecipitacao_CJ_Completo, lstPrecipitacao_SLP_Completo, lstPrecipitacao_Tbt_Completo]
print("lista 3d", lista_precipitacao_completa[0][0])
# Calculando normal provisória de São José dos Campos
#_______________________________________________________________________________________________________________________________________
# Realizando Filtros
lst_Dados_Precipitacao_Tbt = list(filter(lambda x : not x.split("-")[0] == "nan", lst_Dados_Precipitacao_Tbt))
lst_Dados_Precipitacao_CJ = list(filter(lambda x : not x.split("-")[0] == "nan", lst_Dados_Precipitacao_CJ))
lst_Dados_Precipitacao_SLP = list(filter(lambda x : not x.split("-")[0] == "nan", lst_Dados_Precipitacao_SLP))

print(lst_Dados_Precipitacao_Tbt)

# Calculando média
media_mes_Tbt = [ "Mês - " + str(x) + " - " +  str(statistics.mean(list(map(lambda k : float(k.split("-")[0]),filter(lambda y: y.split("-")[1].lstrip("0") == str(x), lst_Dados_Precipitacao_Tbt))))) for x in range(1, 13)]
media_mes_SLP = [ "Mês - " + str(x) + " - " +  str(statistics.mean(list(map(lambda k : float(k.split("-")[0]),filter(lambda y: y.split("-")[1].lstrip("0") == str(x), lst_Dados_Precipitacao_SLP))))) for x in range(1, 13)]
media_mes_CJ = [ "Mês - " + str(x) + " - " +  str(statistics.mean(list(map(lambda k : float(k.split("-")[0]),filter(lambda y: y.split("-")[1].lstrip("0") == str(x), lst_Dados_Precipitacao_CJ))))) for x in range(1, 13)]
medias = [media_mes_CJ, media_mes_SLP, media_mes_Tbt]
print ("Média de Campos do Jordão" ,media_mes_CJ)

normal_SJC = [ "Normal para o mês em SJC: " + str(x+1) + " - " + str((wTbt*float(media_mes_Tbt[x].split("-")[-1])) + (wCJ*float(media_mes_CJ[x].split("-")[-1])) + (wSPT*float(media_mes_SLP[x].split("-")[-1]))) for x in range (0, 12)]
#____________________________________________________________________________________________________________________________________________

print(normal_SJC)

# Calculando pesos
listaAltitude = [alt_CJ, alt_SPT, alt_Tbt]
listaDistancia = [dCJ, dSPT, dTbt]
lista_peso_bruto = []
for  indice, x in enumerate(["Campos do jordão", "SLP","Taubaté"]):
    print(indice)
    peso_bruto = 0.5 * np.exp(0.08*((listaAltitude[indice] - alt_SJC) / 100))
    print(peso_bruto)
    lista_peso_bruto.append(peso_bruto)

lista_pesoNormalizado = [ x / sum(lista_peso_bruto) for x in lista_peso_bruto]
print(lista_pesoNormalizado)

normal_sintetica_SJC = [sum([lista_pesoNormalizado[y] *float([media_mes_CJ, media_mes_SLP, media_mes_Tbt][y][x].split("-")[-1]) for y in range(0, 3)]) for x in range(0, 12)]
print("Normal sintética - ", normal_sintetica_SJC)

pre_202n = {x : [sum([lista_pesoNormalizado[z]*(normal_sintetica_SJC[y]/float(medias[z][y].split("-")[-1]))*float(lista_precipitacao_completa[z][x][y]) for z in range(0, 3)]) for y in range(0, 12)] for x in [0,1, 2,3,4]}
print(pre_202n)

df = pd.DataFrame(pre_202n)
df = pd.DataFrame({x:[df[x][y] if int(df[x][y]) !=102 else normal_sintetica_SJC[y] for y in range(12)] for x in range(5)})
print(df[1])
df.to_excel("C:\\Users\\Pc\\Desktop\\Organizacao_Meus_Docs\\Univap\\Ciencias_Biologicas\\TG1" + "\\teste.xlsx")
