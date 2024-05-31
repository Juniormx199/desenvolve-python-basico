def remove_pontuacao(palavra):
    return "".join([i for i in palavra if i.isalpha()])

with open("frase.txt", "r") as arquivo:
    conteudo = arquivo.read()

with open("palavras.txt", "w") as palavras:
   for i in conteudo.split():
        palavras.write(remove_pontuacao(i) + '\n')

