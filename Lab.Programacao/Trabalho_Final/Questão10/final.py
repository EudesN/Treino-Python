# 1. Importar bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MaxNLocator

# 2. Carregar o conjunto de dados a partir da URL
url = 'https://raw.githubusercontent.com/armandossrecife/lp20231/refs/heads/main/top-500-movies.csv'
df_movies = pd.read_csv(url)

# 3. Limpeza e Preparação dos Dados
df_movies_limpo = df_movies.fillna(df_movies.mean(numeric_only=True))
df_movies_limpo['year'] = df_movies_limpo['year'].astype(int)

# 4. Análise de Série Temporal
ano_inicio = 2000
df_periodo = df_movies_limpo[df_movies_limpo['year'] >= ano_inicio].copy()
bilheteria_anual = df_periodo.groupby('year')['worldwide_gross'].sum().sort_index()

# 5. Criar e Exibir o Gráfico de Linha
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(14, 8))

# Plotta a linha principal, representando os dados anuais
ax.plot(bilheteria_anual.index, bilheteria_anual.values, marker='o', linestyle='-', color='#005a9c')

# Título e rótulos
ax.set_title(f'Evolução da Bilheteria Mundial Anual ({ano_inicio} - {bilheteria_anual.index.max()})', fontsize=18, pad=20)
ax.set_xlabel('Ano de Lançamento', fontsize=12)
ax.set_ylabel('Bilheteria Mundial Total', fontsize=12)

# Função para formatar o eixo Y em bilhões
def formatar_bilhoes(x, pos):
    return f'${x*1e-9:.0f}B'
ax.yaxis.set_major_formatter(FuncFormatter(formatar_bilhoes))

# Garante que os anos no eixo X sejam números inteiros e rotaciona
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()