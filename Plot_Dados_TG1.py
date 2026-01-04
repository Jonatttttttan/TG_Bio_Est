import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from torch.return_types import qr

caminho = "C:\\Users\\Pc\\Desktop\\Organizacao_Meus_Docs\\Univap\\Ciencias_Biologicas\\TG1\\dados_epidemiologicos_formatados.xlsx"
caminho2 = "C:\\Users\\Pc\\Desktop\\Organizacao_Meus_Docs\\Univap\\Ciencias_Biologicas\\TG1\\teste.xlsx"

df = pd.read_excel(caminho, sheet_name="CasosXClima")
df2 = pd.read_excel(caminho2)

qtd_Casos = list(df["qtd_casos"])
semanas = list(df["semana"])

dic = {x : list(map(lambda t: str(qtd_Casos[int(t.split("-")[-1])]) + "|" + semanas[int(t.split("-")[-1])],filter(lambda u : u.split("-")[0] == x,map(lambda y : str(y[1]) + "-" + str(y[0]), enumerate(semanas))))) for x in ["2022", "2023", "2024"]}
# O método acima retorna um dicionário como o ano de chave e uma lista de quantidades como valor
print(dic["2022"])

qtd_Casos_2022 = [sum(map(lambda u: int(u.split("|")[0]),filter(lambda y: int(y.split("-")[1]) == x,  dic["2024"]))) for x in range(1, 13)]
meses_Casos_2022 = [x for x in range(1, 13)]
#precipitacao = df.loc[:,["2022", "2023", "2024"]]
print(qtd_Casos_2022[0]) # Janeiro a Dezembro

print(qtd_Casos_2022)




# Covariância Casos X Precipitação
precipitacao_2022 = list(map(lambda x: int(x), df2[2024]))
print(precipitacao_2022)
covariancia = np.cov(qtd_Casos_2022, precipitacao_2022)
print(covariancia)

# Coeficiente de Rank
coef_Pearson = np.corrcoef(qtd_Casos_2022, precipitacao_2022)
print("Correlação -", coef_Pearson)
# Casos por mês Excel
dic_Casos_ = {x : [sum(map(lambda t: int(t.split("|")[0]), filter(lambda y: int(y.split("-")[1]) == h, dic[x]))) for h in range(1, 13)]  for x in ["2022", "2023", "2024"]}
dic_Casos_["Preciitacao-2022"] = list(map(lambda x: int(x), df2[2022]))
dic_Casos_["Precipitacao-2023"] = list(map(lambda x: int(x), df2[2023]))
dic_Casos_["Precipitacao-2024"] = list(map(lambda x: int(x), df2[2024]))

df_toExcel = pd.DataFrame(dic_Casos_)
df_toExcel.to_excel("C:\\Users\\Pc\\Desktop\\Organizacao_Meus_Docs\\Univap\\Ciencias_Biologicas\\TG1\\CasosXPrecipitacao.xlsx")
print(dic_Casos_["2022"])

# Plotar gráficos

fig, ax = plt.subplots(figsize=(14, 6))
# ax.scatter(precipitacao_2022,qtd_Casos_2022) Gráfico de pontos
ax.plot(meses_Casos_2022,precipitacao_2022) # Gráfico de linhas
ax.tick_params(axis="both", labelsize=16)

ax.set_xlabel("Meses", fontsize=18)
ax.set_ylabel("Precipitação", fontsize=18)
ax.set_title("Meses X Precipitação 2024", fontsize=20)
ax.grid(True, linestyle="--", alpha=0.4)
plt.xticks(rotation=45) # Deixa labels na diagonal
fig.tight_layout()
plt.show()

