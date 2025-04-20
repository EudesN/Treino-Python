cores1 = {"vermelho", "azul", "verde"}
cores2 = {"amarelo", "azul", "laranja"}
cores3 = {"azul", "verde", "preto"}

def selConjunto():
    try:
        print("\nEscolha dois entre os conjuntos 1,2 e 3: ")
        a = int(input("Selecione o primeiro conjunto: "))
        b = int(input("Selecione o segundo conjunto: "))
        if(a not in [1, 2, 3] or b not in [1, 2, 3]):
            print("Conjunto inválido")
            return None, None
        conjuntos = {1: cores1, 2: cores2, 3: cores3}
        return conjuntos[a], conjuntos[b]
    
    except ValueError:
        print("seleção inválida")
        return None, None


while True:

    print("\nMenu de opções:")
    print("1 - União entre dois conjuntos")
    print("2 - Interseção entre dois conjuntos")
    print("3 - Diferença entre dois conjuntos")
    print("4 - Sair do programa")

    opcao = input("Informe a opção: ")

    if opcao == '1':
        conj1, conj2 = selConjunto()
        if conj1 is not None and conj2 is not None:
            resultado = c1.union(c2)
            print("Resultado da união:", resultado)




