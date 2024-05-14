numero_pessoas = int(input("Informe o numero de pessoas entrevistadas: "))
cont = 1
idade_total = 0

while cont <= numero_pessoas:
    idade_total += int(input(f"Digite a idade da pessoa {cont}: "))
    cont += 1
print(f"Idade media é {idade_total / numero_pessoas:.2f} anos")