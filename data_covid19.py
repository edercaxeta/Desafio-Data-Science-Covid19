import pandas as pd
import matplotlib.pyplot as plt

uri = "https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-cities.csv"
dados = pd.read_csv(uri)

# Cidade com mais casos de covid
cidade_mais_casos = dados.loc[dados['totalCases'].idxmax()]

# Cidade com menos casos de covid
cidade_menos_casos = dados.loc[dados['totalCases'].idxmin()]

# Estado com mais casos de covid
estado_mais_casos = dados.groupby('state')['totalCases'].sum().idxmax()

# Estado com menos casos de covid
estado_menos_casos = dados.groupby('state')['totalCases'].sum().idxmin()

# Cidade com mais mortes por covid
cidade_mais_mortes = dados.loc[dados['deaths'].idxmax()]

# Cidade com menos mortes por covid
cidade_menos_mortes = dados.loc[dados['deaths'].idxmin()]

# Estado com mais mortes por covid
estado_mais_mortes = dados.groupby('state')['deaths'].sum().idxmax()

# Estado com menos mortes por covid
estado_menos_mortes = dados.groupby('state')['deaths'].sum().idxmin()

# Total de casos de covid no Brasil
total_casos_brasil = dados['totalCases'].sum()

# Total de mortes por covid no Brasil
total_mortes_brasil = dados['deaths'].sum()

# Gerar um gráfico barplot com 5 estados com mais mortes
top_5_estados_mortes = dados.groupby('state')['deaths'].sum().nlargest(5)
top_5_estados_mortes.plot(kind='bar', title='Top 5 Estados com Mais Mortes por COVID-19')
plt.xlabel('Estado')
plt.ylabel('Número de Mortes')
plt.show()

# Gerar um gráfico histograma com 5 estados com menos mortes
bottom_5_estados_mortes = dados.groupby('state')['deaths'].sum().nsmallest(5)
bottom_5_estados_mortes.plot(kind='bar', title='Top 5 Estados com Menos Mortes por COVID-19')
plt.xlabel('Estado')
plt.ylabel('Número de Mortes')
plt.show()

print(f"Cidade com mais casos de covid: {cidade_mais_casos['city']} com {cidade_mais_casos['totalCases']} casos")
print(f"Cidade com menos casos de covid: {cidade_menos_casos['city']} com {cidade_menos_casos['totalCases']} casos")
print(f"Estado com mais casos de covid: {estado_mais_casos}")
print(f"Estado com menos casos de covid: {estado_menos_casos}")
print(f"Cidade com mais mortes por covid: {cidade_mais_mortes['city']} com {cidade_mais_mortes['deaths']} mortes")
print(f"Cidade com menos mortes por covid: {cidade_menos_mortes['city']} com {cidade_menos_mortes['deaths']} mortes")
print(f"Estado com mais mortes por covid: {estado_mais_mortes}")
print(f"Estado com menos mortes por covid: {estado_menos_mortes}")
print(f"Total de casos de covid no Brasil: {total_casos_brasil}")
print(f"Total de mortes por covid no Brasil: {total_mortes_brasil}")