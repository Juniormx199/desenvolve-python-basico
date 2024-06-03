import random

def chunks(lista, n):
    for i in range(0, len(lista), n):
        yield lista[i:i + n]

with open("gabarito_forca.txt" , "r") as arquivo:
    palavras = arquivo.readlines()
    palavra = palavras[random.randint(0,len(palavras) - 1)].strip()
    print(palavra)

with open("gabarito_enforcado.txt" , "r") as arquivo:
    linhas = arquivo.readlines()
    fase = list(chunks(linhas, 6))
   
resposta = []
for i in range(len(palavra)):
    resposta.append("_")


erros = 0
while True:
    if erros == 7: break
    print(" ".join(resposta))
    letra = input("Digite uma letra: ")
    if letra in palavra:
        for i in range(len(palavra)):
            if i == palavra[i]:
                resposta[i] =  palavra[i]
    else:
        erros += 1
        print("".join(fase[erros - 1]))
