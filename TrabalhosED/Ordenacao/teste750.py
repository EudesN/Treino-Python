import re
import time
from typing import List, Dict, Tuple


def ler_arquivo(nome_arquivo: str) -> List[str]:
    with open(nome_arquivo, 'r', encoding='utf-8') as file:
        conteudo = file.read()
    palavras = re.findall(r'\b[a-zA-Z]+\b', conteudo.lower())
    return palavras


def bubble_sort(lista: List[str]) -> List[str]:
    n = len(lista)
    print("🔄 Iniciando ordenação com Bubble Sort...")
    for i in range(n):
        if i % (n // 20 + 1) == 0:
            progresso = (i / n) * 100
            print(f"Progresso: {progresso:.1f}%")
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    print("✅ Ordenação concluída.")
    return lista


def testar_algoritmo(arquivos: List[str]) -> Tuple[List[Dict[str, str]], List[float]]:
    resultados = []
    tempos = []

    for arquivo in arquivos:
        print(f"\n📁 Lendo arquivo: {arquivo}")
        palavras = ler_arquivo(arquivo)

        print(f"📦 Total de palavras: {len(palavras)}")

        start_time = time.time()
        palavras_ordenadas = bubble_sort(palavras)
        tempo = time.time() - start_time

        resultado = {
            "Arquivo": arquivo,
            "Palavras": str(len(palavras)),
            "Tempo (s)": f"{tempo:.6f}"
        }

        resultados.append(resultado)
        tempos.append(tempo)

        # Mostra resultado após processar cada arquivo
        print("\n📊 RESULTADO PARCIAL")
        imprimir_tabela([resultado])

    return resultados, tempos


def imprimir_tabela(resultados: List[Dict[str, str]]):
    print("\n+-----------------+------------+-------------+")
    print("| Arquivo         | Palavras   | Tempo (s)   |")
    print("+-----------------+------------+-------------+")
    for resultado in resultados:
        print(f"| {resultado['Arquivo']:<15} | {resultado['Palavras']:<10} | {resultado['Tempo (s)']:<11} |")
    print("+-----------------+------------+-------------+")


def main():
    arquivos = ["nomes250k.txt", "nomes500k.txt", "nomes750k.txt"]

    print("⏳ Testando Bubble Sort (otimizado com barra leve)...")
    resultados, tempos = testar_algoritmo(arquivos)

    print("\n📊 RESULTADOS FINAIS (Bubble Sort Otimizado)")
    imprimir_tabela(resultados)

    print("\nℹ️ Dados para análise:")
    print("Arquivos:", ', '.join(arquivos))
    print("Tempos:", ', '.join(f"{t:.6f}" for t in tempos))


if __name__ == "__main__":
    main()
