import random

lista= []
intervalo_maior = []
index_intervalo = 0

for i in range(20):lista.append(random.randint(-10,10))

#for para percorrer a lista 
for y in range(len(lista)):
    #if para saber se o elemento atual e negativo
    if lista[y] < 0:
        #se for negativo vai começar por ele
        start = y     
        #for para verificar quantos elementos negativos tem apos o elemento de inicio 
        for x in range(len(lista[y:])):
            lista_auxiliar = lista[start:]
            if lista_auxiliar[x] > 0:
                break
            else: fim = x + 1
        #if para salvar o index do maior intervalo
        if(start + fim) - start > index_intervalo:
            index_intervalo = (start + fim) - start
            index_inicio = start
            index_final = start + fim

#mostra o resultado
print(lista)
del lista[index_inicio:index_final]
print(lista)






