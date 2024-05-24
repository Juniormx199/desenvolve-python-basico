lista = []

quantidade = int(input("Quantos numeros você quer adicionar a lista (minimo 4) ? "))

if quantidade < 4 : quantidade = 4

for i in range(quantidade):
    lista.append(int(input()))

print(f"A lista original: {lista}")
print(f"Os 3 primeiros elementos: {lista[0:3]}")
print(f"Os 2 últimos elementos: {lista[:-3:-1]}")
print(f"A lista invertida: {lista[::-1]}")
print(f"Os elementos de índice par: {lista[0::2]}")
print(f"Os elementos de índice ímpar: {lista[1::2]}")
