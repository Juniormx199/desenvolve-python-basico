quantidade_experimentos = int(input("Informe a quantidade de experimentos realizados: "))
cont = 1
total_sapos = 0
total_ratos = 0
total_coelho = 0
total_cobaias = 0

print("Preencha a quantidade e o tipo (ex: 10 S), Tipos: S = sapo , C = coelhos , R = ratos ")

while cont <= quantidade_experimentos:
    resposta = input(f"Quantidade e o tipo do experimento {cont}: ")
    lista = resposta.split(" ")
    total_cobaias += int(lista[0])
    cont+= 1
    if lista[1].lower() == 's':
        total_sapos += int(lista[0])

    elif lista[1].lower() == 'r':
        total_ratos += int(lista[0])

    elif lista[1].lower() == 'c':
        total_coelho += int(lista[0])
    else:
        print("Tipo não encontrado!!!")

print(f"Total: {total_cobaias} cobaias")
print(f"Total de coelhos: {total_coelho}")
print(f"Total de ratos: {total_ratos}")
print(f"Total de sapos: {total_sapos}")
print(f"Percentual de coelhos {(total_coelho / total_cobaias) * 100:.2f} %")
print(f"Percentual de ratos {(total_ratos / total_cobaias) * 100:.2f} %")
print(f"Percentual de sapos {(total_sapos / total_cobaias) * 100:.2f} %")