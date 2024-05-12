valor = int(input("Digite um valor inteiro em reais: "))

quantidade_cedulas = valor // 100
valor -= quantidade_cedulas * 100
print(f"{quantidade_cedulas} nota(s) de R$100,00")

quantidade_cedulas = valor // 50
valor -= quantidade_cedulas * 50
print(f"{quantidade_cedulas} nota(s) de R$50,00")

quantidade_cedulas = valor // 20
valor -= quantidade_cedulas * 20
print(f"{quantidade_cedulas} nota(s) de R$20,00")

quantidade_cedulas = valor // 10
valor -= quantidade_cedulas * 10
print(f"{quantidade_cedulas} nota(s) de R$10,00")

quantidade_cedulas = valor // 5
valor -= quantidade_cedulas * 5
print(f"{quantidade_cedulas} nota(s) de R$5,00")

quantidade_cedulas = valor // 2
valor -= quantidade_cedulas * 2
print(f"{quantidade_cedulas} nota(s) de R$2,00")

quantidade_cedulas = valor // 1
valor -= quantidade_cedulas * 1
print(f"{quantidade_cedulas} nota(s) de R$1,00")