cod, quant = map(int, input().split())
if cod == 1:
     tot = 4 * quant

if cod == 2:
    tot = 4.5 * quant

if cod == 3:
    tot = 5 * quant

if cod == 4:
    tot = 2 * quant

if cod == 5:
    tot = 1.5 * quant
print(f"Total: R$ {tot:.2f}")