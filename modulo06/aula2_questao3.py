import random

lista1 = []
lista2 = []
interseccao = []


for i in range(20):
    lista1.append(random.randint(0,50))
    lista2.append(random.randint(0,50))

for x in range(len(lista1)):
    if lista1[x] in lista2:
        if lista1[x] not in interseccao:
            interseccao.append(lista1[x])

print(f"lista 1-{lista1}")
print(f"lista 2-{lista2}")
print(f"Interseccao -{interseccao}")
print("Contagem")

for y in range(len(interseccao)):
    print(f"{interseccao[y]}:(lista 1 ={lista1.count(interseccao[y])} , lista 2 ={lista2.count(interseccao[y])})")