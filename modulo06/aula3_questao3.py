lista = [9, 2, -1, -4, -2, -3, 5, 6, -7, -4, -1, 6, 8, -3, -6,-4,-2,-4]

fim = 0
start = 0
intervalo_maior = []
intervalo = 0
inicio = 0
final = 0

for y in range(len(lista)):
    if lista[y] < 0:
        start = y        
        for x in range(len(lista[y:])):
            lista_auxiliar = lista[start:]
            if lista_auxiliar[x] > 0:
                break
            else: fim = x + 1
        if(start + fim) - start > intervalo:
            intervalo = (start + fim) - start
            inicio = start
            final = start + fim


print(lista)
print(lista[inicio:final:])

del lista[inicio:final]

print(lista)






