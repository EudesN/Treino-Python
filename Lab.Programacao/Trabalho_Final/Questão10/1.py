import pandas as pd
import matplotlib.pyplot as plt

# 1. Carrega e limpa os dados
url = 'https://raw.githubusercontent.com/armandossrecife/lp20231/refs/heads/main/top-500-movies.csv'
df = pd.read_csv(url)
df = df.fillna(df.mean(numeric_only=True))
df['genre'] = df['genre'].fillna('Outro')  # evita chained assignment

# 2. Soma e calcula percentuais
arrecada = df.groupby('genre')['worldwide_gross'].sum()
total = arrecada.sum()
pct = (arrecada / total) * 100
pct = pct.sort_values(ascending=False)

# 3. Agrupa gêneros com <2% em 'Outros'
limite = 2.0
grandes = pct[pct >= limite]
pequenos = pct[pct < limite].sum()
pct_corrigido = pd.concat([grandes, pd.Series({'Outros': pequenos})])

# 4. Desenha o gráfico de pizza
plt.figure(figsize=(10, 8))

# explode só a fatia 'Outros' para destacá-la
explode = [0.02 if g != 'Outros' else 0.1 for g in pct_corrigido.index]

wedges, texts, autotexts = plt.pie(
    pct_corrigido,
    labels=pct_corrigido.index,   # rótulos com o nome do gênero
    autopct='%1.1f%%',             # mostra o percentual dentro da fatia
    startangle=140,
    explode=explode,
    pctdistance=0.6,               # distancia do texto %=0.6 do centro
    labeldistance=1.1,             # distancia dos rótulos: >1 afasta para fora
    wedgeprops={'linewidth': 0.5, 'edgecolor': 'white'}
)

# 5. Ajustes finais
plt.title('Participação Percentual da Bilheteria Mundial por Gênero', fontsize=16)
plt.axis('equal')   # círculo perfeito
plt.tight_layout()  # ajusta margens para os rótulos caberem
plt.show()
