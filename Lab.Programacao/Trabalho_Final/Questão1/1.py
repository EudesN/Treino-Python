# 1. Importar bibliotecas
import pandas as pd
import matplotlib.pyplot as plt

# 2. Carregar o conjunto de dados a partir da URL
url = 'https://raw.githubusercontent.com/armandossrecife/lp20231/refs/heads/main/top-500-movies.csv'
df_movies = pd.read_csv(url)

# 3. Limpeza e Preparação dos Dados
# Preenche valores numéricos ausentes (NaN) com a média da coluna
df_movies_limpo = df_movies.fillna(df_movies.mean(numeric_only=True))

# 4. Selecionar os 20 filmes com maior bilheteria mundial
filmes_maior_bilheteria = df_movies_limpo.sort_values('worldwide_gross', ascending=False).head(20)

# Para o gráfico horizontal, é melhor ordenar do menor para o maior,
# assim o maior valor aparece no topo do gráfico.
filmes_grafico = filmes_maior_bilheteria.sort_values('worldwide_gross', ascending=True)

# Extrair os títulos e os valores de arrecadação
titulos = filmes_grafico['title']
arrecadacao = filmes_grafico['worldwide_gross']


# 5. Criar e Exibir o Gráfico de Barras Horizontais
plt.style.use('seaborn-v0_8-talk') # Usar um estilo visualmente agradável
fig, ax = plt.subplots(figsize=(12, 10)) # Criar a figura e os eixos

# Cria as barras horizontais
bars = ax.barh(titulos, arrecadacao, color='#3498db')

# Título e rótulos dos eixos
ax.set_title('Top 20 Filmes por Bilheteria Mundial', fontsize=18, pad=20)
ax.set_xlabel('Bilheteria Mundial (em bilhões de dólares)', fontsize=12)
ax.set_ylabel('Filme', fontsize=12)

# Formatar os números do eixo X para ficarem mais legíveis (ex: 2.5B em vez de 2,500,000,000)
def formatar_bilhoes(x, pos):
    return f'{x*1e-9:.1f}B' # Converte o número para bilhões com 1 casa decimal
from matplotlib.ticker import FuncFormatter
ax.xaxis.set_major_formatter(FuncFormatter(formatar_bilhoes))

# Remover as bordas do gráfico para um visual mais limpo
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

# Adicionar os valores no final de cada barra para clareza
for bar in bars:
    width = bar.get_width()
    label_x_pos = width + 1e8 # Posição um pouco à frente da barra
    ax.text(label_x_pos, bar.get_y() + bar.get_height()/2, f'{width*1e-9:.2f}B',
            va='center', ha='center', fontsize=10)


plt.tight_layout() # Ajusta o layout para evitar cortes
plt.show() # Exibe o gráfico