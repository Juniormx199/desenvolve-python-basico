import random
lista = []

for i in range(20):
    lista.append(random.randint(-100,100))


print("\nA lista ordenada, sem modificar a lista original\n" , sorted(lista))
print("\nA lista original\n" , lista)
print("\nO índice do maior valor da lista original\n" , lista.index(max(lista)))
print("\nO índice do menor valor da lista original\n" , lista.index(min(lista)))