import pandas as pd
import matplotlib.pyplot as plt

# 1. Carregar os dados
url = 'https://raw.githubusercontent.com/armandossrecife/lp20231/refs/heads/main/top-500-movies.csv'
df = pd.read_csv(url)

# 2. Limpeza
# 2.1 Preenche NaN numéricos com a média da coluna
df = df.fillna(df.mean(numeric_only=True))

# 2.2 Preenche NaN de gênero com 'Outro' 
#    -> substitui inplace para evitar chained assignment warning
df['genre'] = df['genre'].fillna('Outro')

# 3. Soma da bilheteria por gênero
arrecada = df.groupby('genre')['worldwide_gross'].sum()

# 4. Percentuais
total = arrecada.sum()
pct = (arrecada / total) * 100
pct = pct.sort_values(ascending=False)

# 5. Agrupar fatias pequenas em 'Outros'
limite = 2.0  # percentuais abaixo de 2% serão consolidados
grandes = pct[pct >= limite]
pequenos = pct[pct < limite].sum()

#    -> usa pd.concat em vez de append
pct_corrigido = pd.concat([
    grandes,
    pd.Series({'Outros': pequenos})
])

# 6. Plotagem
plt.figure(figsize=(10, 8))
explode = [0.02 if genre != 'Outros' else 0.1 for genre in pct_corrigido.index]

wedges, textos, autotextos = plt.pie(
    pct_corrigido,
    labels=None,
    autopct='%1.1f%%',
    startangle=140,
    pctdistance=0.7,
    explode=explode,
    wedgeprops={'linewidth': 0.5, 'edgecolor': 'white'}
)

plt.legend(
    wedges,
    pct_corrigido.index,
    title='Gêneros',
    bbox_to_anchor=(1, 0, 0.5, 1),
    loc='center left'
)

plt.title('Participação Percentual da Bilheteria Mundial por Gênero', fontsize=16)
plt.axis('equal')
plt.tight_layout()
plt.show()
