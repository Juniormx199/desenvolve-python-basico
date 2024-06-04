import csv

def busca_top(ano, dados):
    maior_reproducao = 0
    top = []
    for linha in dados:
        if linha[3] == ano:
            reproducoes = int(linha[8])
            if reproducoes > maior_reproducao:
                maior_reproducao = reproducoes
                top = linha[:2] + linha[3:4] + linha[8:9]
    return top

with open("spotify-2023.csv", "r", encoding='latin-1') as arquivo:
    dados = list(csv.reader(arquivo, delimiter=',', quotechar='"'))

ano_inicial = int(input("Ano inicial: "))
ano_final = int(input("Ano final: "))

mais_tocadas = []

for ano in range(ano_inicial, ano_final + 1):
    mais_tocadas.append(busca_top(str(ano), dados))

for musica in mais_tocadas:
    print(musica)