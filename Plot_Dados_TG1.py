import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

caminho = "C:\\Users\\Pc\\Desktop\\Organizacao_Meus_Docs\\Univap\\Ciencias_Biologicas\\TG1\\dados_epidemiologicos_formatados.xlsx"

df = pd.read_excel(caminho, sheet_name="CasosXClima")


X = list(df["qtd_casos"])

y_ = list(filter(lambda y : str(y).split("-")[1]=="2022",list(map(lambda x: str(x[0]) + "-" +str(x[1]) , enumerate(df["semana"])))))
X = list(filter(lambda x: x.split("-")[0] in list(map(lambda u: u.split("-")[0], y_)), list(map(lambda y : str(y[0]) + "-" + str(y[1]), enumerate(X)))))


semana = list(map(lambda x: x.split("-")[0], y_))
casos = list(map(lambda x: int("-".join(x.split("-")[1:])), X))
semana = [ "Sem - " + str(x) for x in range(1, len(semana)+1)]
print(semana)
print(type(casos[0]))



fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(semana, casos, marker='o', linewidth=2)



ax.set_xlabel("Semana do ano 2022")
ax.set_ylabel("Casos de dengue")
ax.set_title("Casos X Semana")
ax.grid(True, linestyle="--", alpha=0.4)
#plt.xticks(semana)
fig.tight_layout()
plt.show()


'''
# Próximas etapas
  - Deixar labels do eix X na diagonal;
  - Plotar gráficos de casos X precipitação
    - Somar casos por mês
  - Passar para word

'''

