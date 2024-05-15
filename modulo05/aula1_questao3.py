import random

n = random.randint(1,10)

while True:
    numero =int(input("Adivinhe o número entre 1 e 10: "))
    if numero > n:
        print("Muito alto, tente novamente!")
    elif numero < n :
        print("Muito baixo, tente novamente!")
    else:
        print(f"Correto! O número é {n}")
        break