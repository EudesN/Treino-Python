
def calculoArea(terreno):
    base, alt = terreno
    return base * alt

terreno = []

for i in range(3):
    print(f"Informações do terreno {i + 1}")
    base = float(input("Informe a base: "))
    alt = float(input("Informe o valor da altura: "))
    terreno.append((base, alt))

print("Terrenos: ")
for i, terreno in enumerate(terreno, 1):
    print(f"Terreno {i}: Base = {terreno[0]}m, Altura = {terreno[1]}m")

areas = [calculoArea(terreno) for terra in terreno]

maior = max(areas)
menor = min(areas)

print(f"\nA maior área é: {maior} m²")
print(f"A menor área é: {menor} m²")





