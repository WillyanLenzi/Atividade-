total = 0

for i in range(8):
    preco = float(input(f"Digite o preço do {i + 1}º produto: R$ "))
    total += preco

print(f"Valor final da compra: R$ {total:.2f}")
