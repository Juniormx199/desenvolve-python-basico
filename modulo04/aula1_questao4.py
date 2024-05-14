n = int(input("Digite o valor de n: "))
maior = 0

while n > 0:
    x = int(input("Digite o valor de x: "))
    if x > maior:
        maior = x
    n = n - 1
print(maior)    