with open("frase.txt", "r") as arquivo:
    conteudo = arquivo.read()

with open("palavras.txt", "w") as palavras:
   for i in conteudo.split():
        palavras.write(i + '\n')

