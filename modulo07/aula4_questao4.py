import random


def imprime_enforcado(erros, fases):
    return "".join(fases[erros])

with open("gabarito_enforcado.txt", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()
    fases = [linhas[i:i + 6] for i in range(0, len(linhas), 6)]

with open("gabarito_forca.txt", "r", encoding="utf-8") as arquivo:
    palavras = arquivo.readlines()
    palavra = palavras[random.randint(0, len(palavras) - 1)].strip().lower()

erros = 0
resposta = ["_" for _ in range(len(palavra))]
letras_erradas = []
letras_corretas = []

while True:
    print("\n")
    print(imprime_enforcado(erros, fases))
    
    if erros == 6: 
        print(f"Game Over, a palavra era '{palavra}'")
        break

    if palavra == "".join(resposta):
        print("Você ganhou!!!")
        break
   
    print(" ".join(resposta))
    print(f"Letras erradas: {', '.join(letras_erradas)}")

    letra = input("\nDigite uma letra: ").lower()

    if len(letra) != 1 or not letra.isalpha():
        print("Entrada invalida! Digite apenas uma letra.")
        continue

    if letra in letras_corretas or letra in letras_erradas:
        print("Você ja tentou essa letra. Tente uma diferente.")
        continue

    if letra in palavra:
        letras_corretas.append(letra)
        for i in range(len(palavra)):
            if letra == palavra[i]:
                resposta[i] = letra
    else:
        letras_erradas.append(letra)
        erros += 1