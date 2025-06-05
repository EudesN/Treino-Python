import matplotlib.pyplot as plt
import numpy as np

tamanhos = ['250K', '500K', '750K']
tempo_bubble = [837.534, 3156.794, 10275.769]
tempo_selection = [248.542, 865.964, 2923.18]
tempo_insertion = [226.841, 738.987, 1809.573]

x = np.arange(len(tamanhos))
largura = 0.25

bar1= plt.bar(x - largura, tempo_bubble, width=largura, label='Bubble Sort')
bar2= plt.bar(x, tempo_selection, width=largura, label='Selection Sort')
bar3= plt.bar(x + largura, tempo_insertion, width=largura, label='Insertion Sort')

plt.bar_label(bar1, padding=3, fontsize=8)
plt.bar_label(bar2, padding=3, fontsize=8)
plt.bar_label(bar3, padding=3, fontsize=8)

plt.xticks(x, tamanhos)
plt.xlabel("Tamanho da lista")
plt.ylabel("Tempo (segundos)")
plt.title("Tempo Médio de Execução por Tamanho da Lista")
plt.legend()
plt.tight_layout()
plt.show()