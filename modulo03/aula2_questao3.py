idade = int(input("Informe sua idade: "))

quantidade_partidas = input("Já jogou pelo menos 3 jogos de tabuleiro (17responda true ou false) ? ")
quantidade_partidas = (quantidade_partidas.lower() == "true")

quantidade_vitoria = int(input("Quantas vezes venceu um jogo ?"))

print("Apto para ingressar no clube de jogos de tabuleiro:",(idade >= 16 and idade <= 18) and (quantidade_partidas == True) and (quantidade_vitoria >= 1))