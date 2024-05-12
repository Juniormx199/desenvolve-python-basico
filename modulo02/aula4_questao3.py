italic = '\033[3m'
negrito = '\033[1m'
resetar = '\033[0m'

#entrada de dados produto 1
produto1_nome = input(f"{italic}Digite o nome do produto 1:{resetar}")
produto1_preco = float(input(f"{italic}Digite o preço unitário do produto 1: {resetar}")) 
produto1_quantidade = float(input(f"{italic}Digite a quantidade do produto 1: {resetar}"))
#entrada de dados produto 2
produto2_nome = input(f"{italic}Digite o nome do produto 2: {resetar}")
produto2_preco = float(input(f"{italic}Digite o preço unitário do produto 2: {resetar}"))
produto2_quantidade = float(input(f"{italic}Digite a quantidade do produto 1: {resetar}"))
#entrada de dados produto 3
produto3_nome = input(f"{italic}Digite o nome do produto 3: {resetar}")
produto3_preco = float(input(f"{italic}Digite o preço unitário do produto 3: {resetar}"))
produto3_quantidade = float(input(f"{italic}Digite a quantidade do produto 3: {resetar}"))

valor_total= (produto1_preco * produto1_quantidade)+(produto2_preco * produto2_quantidade)+(produto3_preco * produto3_quantidade)
print(f"{italic}Total:{resetar} R${valor_total:,.2f}")