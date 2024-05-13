distancia = float(input("Informe a distancia em km: "))
peso = float(input("Informe o peso em kg: "))
if distancia <= 100:
    valor = peso * 1
elif distancia >= 101 and distancia <= 300:
    valor = peso * 1.50
elif distancia > 300:
    valor = peso * 2
if peso > 10:
    valor+= 10

print(f"Valor do frete : R${valor:,.2f}")