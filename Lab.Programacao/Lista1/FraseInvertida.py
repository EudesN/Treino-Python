frase = str(input("Informe a frase: "))
frase = frase[:100]
fraseInvertida = ""
for l in range(len(frase) -1, -1, -1):
    fraseInvertida += frase[l]
print(fraseInvertida)