import random

def embaralhar_palavras(frase):
    palavras = frase.split(" ")
    frase_modificada = ""
    for palavra in palavras:
        if len(palavra) > 3:
            meio_palavra = list(palavra[1:-1])
            random.shuffle(meio_palavra)
            frase_modificada += palavra[0] + "".join(meio_palavra) + palavra[-1] + " " 
        else:
            frase_modificada += palavra + " "

    return frase_modificada



frase = "Python é uma linguagem de programação"
print(embaralhar_palavras(frase))

