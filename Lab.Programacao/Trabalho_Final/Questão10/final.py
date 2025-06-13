# 1. Importar bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MaxNLocator

# 2. Carregar o conjunto de dados a partir da URL
url = 'https://raw.githubusercontent.com/armandossrecife/lp20231/refs/heads/main/top-500-movies.csv'
df_movies = pd.read_csv(url)

# 3. Limpeza e Preparação dos Dados
# Preenche valores numéricos ausentes (NaN) com a média
df_movies_limpo = df_movies.fillna(df_movies.mean(numeric_only=True))

# Converte a coluna 'year' para inteiro, para garantir que não haja casas decimais
df_movies_limpo['year'] = df_movies_limpo['year'].astype(int)

# 4. Análise de Série Temporal
# Define o período desejado (últimos 25 anos, de 2000 a 2024)
ano_inicio = 2000
df_periodo = df_movies_limpo[df_movies_limpo['year'] >= ano_inicio].copy()

# Agrupa por ano e soma a bilheteria mundial
bilheteria_anual = df_periodo.groupby('year')['worldwide_gross'].sum()

# Garante que os dados estejam ordenados por ano
bilheteria_anual = bilheteria_anual.sort_index()

# 5. Criar e Exibir o Gráfico de Linha
plt.style.use('seaborn-v0_8-whitegrid') # Define um estilo visual
fig, ax = plt.subplots(figsize=(14, 8))

# Plotta a linha principal
ax.plot(bilheteria_anual.index, bilheteria_anual.values, marker='o', linestyle='-', color='b', label='Bilheteria Mundial')

# Adiciona uma linha de tendência (média móvel de 3 anos para suavizar a curva)
media_movel = bilheteria_anual.rolling(window=3).mean()
ax.plot(media_movel.index, media_movel.values, linestyle='--', color='r', label='Tendência (Média Móvel 3 anos)')


# Título e rótulos
ax.set_title(f'Evolução da Bilheteria Mundial Anual ({ano_inicio} - {bilheteria_anual.index.max()})', fontsize=18, pad=20)
ax.set_xlabel('Ano de Lançamento', fontsize=12)
ax.set_ylabel('Bilheteria Mundial Total', fontsize=12)

# Função para formatar o eixo Y em bilhões
def formatar_bilhoes(x, pos):
    return f'${x*1e-9:.0f}B'
ax.yaxis.set_major_formatter(FuncFormatter(formatar_bilhoes))

# Garante que os anos