import re
import time
from typing import List, Dict, Tuple


def ler_arquivo(nome_arquivo: str) -> List[str]:
    """Lê o conteúdo de um arquivo e retorna uma lista de palavras normalizadas (apenas letras minúsculas)."""
    with open(nome_arquivo, 'r', encoding='utf-8') as file:
        conteudo = file.read()
    palavras = re.findall(r'\b[a-zA-Z]+\b', conteudo.lower())
    return palavras


def selection_sort(lista: List[str]) -> List[str]:
    """Ordena a lista usando o algoritmo Selection Sort com barra de progresso leve."""
    n = len(lista)
    print("🔄 Iniciando ordenação com Selection Sort...")
    for i in range(n):
        if i % (n // 20 + 1) == 0:  # Exibe progresso a cada ~5% de avanço
            progresso = (i / n) * 100
            print(f"Progresso: {progresso:.1f}%")
        menor_indice = i
        for j in range(i + 1, n):
            if lista[j] < lista[menor_indice]:
                menor_indice = j
        if menor_indice != i:
            lista[i], lista[menor_indice] = lista[menor_indice], lista[i]
    print("✅ Ordenação concluída.")
    return lista


def testar_algoritmo(arquivos: List[str]) -> Tuple[List[Dict[str, str]], List[float]]:
    """Executa o algoritmo Selection Sort em cada arquivo e mede o tempo de execução."""
    resultados = []
    tempos = []

    for arquivo in arquivos:
        print(f"\n📁 Lendo arquivo: {arquivo}")
        palavras = ler_arquivo(arquivo)

        print(f"📦 Total de palavras: {len(palavras)}")

        start_time = time.time()
        palavras_ordenadas = selection_sort(palavras)
        tempo = time.time() - start_time

        print(f"⏱️ Tempo para ordenar '{arquivo}': {tempo:.6f} segundos")  # Tempo individual exibido

        resultados.append({
            "Arquivo": arquivo,
            "Palavras": str(len(palavras)),
            "Tempo (s)": f"{tempo:.6f}"
        })
        tempos.append(tempo)

    return resultados, tempos


def imprimir_tabela(resultados: List[Dict[str, str]]):
    """Imprime uma tabela com os resultados da ordenação."""
    print("\n+-----------------+------------+-------------+")
    print("| Arquivo         | Palavras   | Tempo (s)   |")
    print("+-----------------+------------+-------------+")
    for resultado in resultados:
        print(f"| {resultado['Arquivo']:<15} | {resultado['Palavras']:<10} | {resultado['Tempo (s)']:<11} |")
    print("+-----------------+------------+-------------+")


def main():
    arquivos = ["nomes250k.txt", "nomes500k.txt", "nomes750k.txt"]  # Substitua pelos nomes corretos dos seus arquivos

    print("⏳ Testando Selection Sort com múltiplos arquivos...")
    resultados, tempos = testar_algoritmo(arquivos)

    print("\n📊 RESULTADOS (Selection Sort)")
    imprimir_tabela(resultados)

    print("\nℹ️ Dados para análise:")
    print("Arquivos:", ', '.join(arquivos))
    print("Tempos:", ', '.join(f"{t:.6f}" for t in tempos))


if __name__ == "__main__":
    main()
