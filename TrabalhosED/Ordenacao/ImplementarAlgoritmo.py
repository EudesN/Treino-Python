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
    ultimo_progresso = -5  # para garantir que 0% seja mostrado

    for i in range(n):
        progresso = int((i / n) * 100)
        if progresso % 5 == 0 and progresso != ultimo_progresso:
            print(f"Progresso: {progresso}%")
            ultimo_progresso = progresso

        trocou = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True
        if not trocou:
            break

    print("Progresso: 100%")
    return lista


def testar_algoritmo(arquivos: List[str]) -> Tuple[List[Dict[str, str]], List[float]]:
    resultados = []
    tempos = []
    
    for arquivo in arquivos:
        print(f"\n📁 Processando arquivo: {arquivo}")
        palavras = ler_arquivo(arquivo)
        
        start_time = time.time()
        palavras_ordenadas = bubble_sort(palavras)
        tempo = time.time() - start_time

        # Mostrar as palavras ordenadas
        print(f"\n🔤 Palavras ordenadas do arquivo {arquivo}:\n")
        print(', '.join(palavras_ordenadas))
        # Se quiser limitar a exibição:
        # print(', '.join(palavras_ordenadas[:50]) + ' ...')

        resultados.append({
            "Arquivo": arquivo,
            "Palavras": str(len(palavras)),
            "Tempo (s)": f"{tempo:.6f}"
        })
        tempos.append(tempo)
    
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
    
    print("⏳ Testando Bubble Sort (versão otimizada)...")
    resultados, tempos = testar_algoritmo(arquivos)
    
    print("\n📊 RESULTADOS (Bubble Sort Otimizado)")
    imprimir_tabela(resultados)
    
    print("\nℹ️ Dados para análise:")
    print("Arquivos:", ', '.join(arquivos))
    print("Tempos:", ', '.join(f"{t:.6f}" for t in tempos))


if __name__ == "__main__":
    main()
