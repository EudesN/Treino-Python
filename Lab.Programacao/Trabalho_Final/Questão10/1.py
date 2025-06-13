import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.ticker import FuncFormatter # Importar o formatador

# 1. Carrega os dados
url = 'https://raw.githubusercontent.com/armandossrecife/lp20231/refs/heads/main/top-500-movies.csv'
df = pd.read_csv(url)

# 2. Converte 'release_date' para datetime (trata erros)
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')

# 3. Cria uma nova coluna com o ano de lançamento
df['ano'] = df['release_date'].dt.year

# 4. Filtra os últimos 25 anos
# Usando o ano atual do seu computador para o cálculo
ano_atual = datetime.now().year 
ultimos_25_anos = df[(df['ano'] >= ano_atual - 25) & (df['ano'] <= ano_atual)]

# 5. Remove valores nulos de bilheteria e também de ano
# É bom garantir que não há anos nulos após a conversão de data
ultimos_25_anos = ultimos_25_anos.dropna(subset=['ano', 'worldwide_gross'])

# 6. Agrupa por ano e soma a bilheteria
arrecadacao_anual = ultimos_25_anos.groupby('ano')['worldwide_gross'].sum()

# 7. Plota o gráfico de série temporal
plt.style.use('seaborn-v0_8-whitegrid')
plt.figure(figsize=(14, 7))
plt.plot(arrecadacao_anual.index, arrecadacao_anual.values, marker='o', color='royalblue', linewidth=2)
plt.title('Evolução da Arrecadação Mundial nos Últimos 25 Anos', fontsize=16)
plt.xlabel('Ano de Lançamento', fontsize=12)
plt.ylabel('Bilheteria Mundial (em bilhões de US$)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)

# ---> MELHORIA ADICIONADA AQUI <---
# Função para formatar o eixo Y em bilhões
def formatar_bilhoes(x, pos):
    return f'${x*1e-9:.0f}B'

# Aplica o formatador ao eixo Y do gráfico
plt.gca().yaxis.set_major_formatter(FuncFormatter(formatar_bilhoes))

# Garante que os anos no eixo X sejam números inteiros
from matplotlib.ticker import MaxNLocator
plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()