import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# 1. Carrega os dados
url = 'https://raw.githubusercontent.com/armandossrecife/lp20231/refs/heads/main/top-500-movies.csv'
df = pd.read_csv(url)

# 2. Converte 'release_date' para datetime (trata erros)
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')

# 3. Cria uma nova coluna com o ano de lançamento
df['ano'] = df['release_date'].dt.year

# 4. Filtra os últimos 25 anos
ano_atual = datetime.now().year
ultimos_25_anos = df[(df['ano'] >= ano_atual - 25) & (df['ano'] <= ano_atual)]

# 5. Remove valores nulos de bilheteria
ultimos_25_anos = ultimos_25_anos.dropna(subset=['worldwide_gross'])

# 6. Agrupa por ano e soma a bilheteria
arrecadacao_anual = ultimos_25_anos.groupby('ano')['worldwide_gross'].sum()

# 7. Plota o gráfico de série temporal
plt.figure(figsize=(12, 6))
plt.plot(arrecadacao_anual.index, arrecadacao_anual.values, marker='o', color='blue', linewidth=2)
plt.title('Evolução da Arrecadação Mundial nos Últimos 25 Anos', fontsize=16)
plt.xlabel('Ano')
plt.ylabel('Bilheteria Mundial (US$)')
plt.grid(True)
plt.tight_layout()
plt.show()
