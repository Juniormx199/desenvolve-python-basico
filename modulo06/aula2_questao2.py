import random

num_elementos = random.randint(5 , 20)
lista = []

for i in range(num_elementos):
    lista.append(random.randint(1,10))

print(f"A lista elementos:{lista}")
print(f"A soma dos valores da lista: {sum(lista)}")
print(f"A média dos valores da lista: {sum(lista) / len(lista):.2f}")