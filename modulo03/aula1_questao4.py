n = float(input("Informe o valor de n: "))
maior = 0
while n > 0 :
    if n > 0 :
        x = float(input("Informe o valor de x: "))
        if x > maior:
            maior = x
        n = n -1
    else:
        print(maior)