lista =['caderno', 'janela', 'telefone', 'mochila', 'abacaxi', 'teclado', 'relógio', 'bicicleta', 'girassol', 'montanha']

encontrou = 0;
palavra = str(input("Informe a palavra: "))

for i in range(len(lista)):
    if(palavra == lista[i]):
        encontrou = 1;
        print("A palavra foi encontrada!")
        break

if(encontrou == 0):
    print("palavra não encontrada!")

