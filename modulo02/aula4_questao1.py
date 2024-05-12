#Entrada do comprimento
comprimento = int(input("Informe o comprimento do terreno:"))
#Entrada do largura
largura = int(input("Informe o largura do terreno:"))
#Entrada do preco do metro quadrado
preco_m2 = float(input("Informe o preço do metro quadrado:"))
#calculo do metro quadrado
area_m2 = comprimento * largura
#calculo do preço total
preco_total = preco_m2 * area_m2
#Mostrar informações na tela
print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")