import random

def encrypt(nome , chave):
    cript = ''
    for i in range(len(nome)):
        letra_cript = ord(nome[i]) + chave
        if letra_cript > 126: 
            letra_cript =  (letra_cript - 126) + 32
        cript += chr(letra_cript)
    return cript

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
chave = random.randint(1,10)
nomes_cript = [encrypt(nomes[i],chave) for i in range(len(nomes))]

print(f"nomes = {nomes}")
print(f"chave_aleatoria = {chave}")
print(f"nomes_cript = {nomes_cript}")
