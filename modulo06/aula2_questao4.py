
lista1 = []
lista2 = []
lista_intercalada = []

for x in range(2):
    quantidade_elementos = int(input(f"Digite a quantidade de elementos da lista {x + 1}: "))
    print(f"Digite os {quantidade_elementos} elementos da lista {x + 1}: ")
    for i in range(quantidade_elementos):
        if x == 0:
            lista1.append(input())
        else:
            lista2.append(input())

tamanho = len(lista1) if len(lista1) > len(lista2) else len(lista2)

for y in range(tamanho):
    if len(lista1)  >= y + 1:
        lista_intercalada.append(lista1[y])
    if len(lista2)  >= y + 1:
        lista_intercalada.append(lista2[y])

print(f"Lista intercalada: {lista_intercalada}")