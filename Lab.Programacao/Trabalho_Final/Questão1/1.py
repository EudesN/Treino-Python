# 1. Importar bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt

# 2. Carregar o conjunto de dados a partir da URL
# O pandas pode ler arquivos CSV diretamente de um link da internet.
url = 'https://raw.githubusercontent.com/armandossrecife/lp20231/refs/heads/main/top-500-movies.csv'
df_movies = pd.read_csv(url)

# 3. Limpeza e Preparação dos Dados
# Preenche valores numéricos ausentes (NaN) com a média da coluna
df_movies_limpo = df_movies.fillna(df_movies.mean(numeric_only=True))
# Preenche valores de gênero ausentes com 'Outro' para que não sejam ignorados
df_movies_limpo['genre'].fillna('Outro', inplace=True)

# 4. Agrupar os dados por gênero e calcular a bilheteria
# Agrupa o DataFrame pela coluna 'genre' e soma a 'worldwide_gross' para cada grupo
arrecadacao_por_genero = df_movies_limpo.groupby('genre')['worldwide_gross'].sum()

# Calcula o percentual de cada gênero sobre o total
total_mundial = arrecadacao_por_genero.sum()
percentuais = (arrecadacao_por_genero / total_mundial) * 100

# Ordena os valores para o gráfico ficar mais organizado
percentuais_ordenado = percentuais.sort_values(ascending=False)

# 5. Criar e exibir o Gráfico de Pizza (ou Rosca)
plt.figure(figsize=(12, 10)) # Define o tamanho do gráfico

# Cria o gráfico de pizza com os dados, rótulos e formatação de percentual
plt.pie(percentuais_ordenado,
        labels=percentuais_ordenado.index,
        autopct='%1.1f%%', # Formato do percentual
        startangle=140,   # Ângulo inicial para melhor visualização
        pctdistance=0.85) # Distância do texto de percentual em relação ao centro

# Opcional: Adiciona um círculo no centro para criar um efeito de "rosca" (donut chart)
centre_circle = plt.Circle((0,0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Título e ajustes finais
plt.title('Participação Percentual da Bilheteria Mundial por Gênero', fontsize=16)
plt.axis('equal')  # Garante que a pizza seja um círculo perfeito
plt.show() # Exibe o gráfico