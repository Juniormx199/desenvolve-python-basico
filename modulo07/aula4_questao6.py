
with open("spotify-2023.csv" ,"r" , encoding='latin-1' ) as arquivo:
    linhas = arquivo.readlines()
    musicas = [linhas[i] for i in range(len(linhas))]