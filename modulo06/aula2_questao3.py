import random
lista1 = []
lista2 = []
interseccao = []


for i in range(5):
    lista1.append(random.randint(0,5))
    lista2.append(random.randint(0,5))

for x in range(len(lista1)):
    if lista1[x] in lista2:
        if lista1[x] not in interseccao:
            interseccao.append(lista1[x])

for y in range(len(interseccao)):
    print(interseccao.count(interseccao[y]))

             
print(lista1)
print(lista2)
print(interseccao)

