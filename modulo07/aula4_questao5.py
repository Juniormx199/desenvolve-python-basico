with open("meus_livros.csv", "w") as arquivo:
    arquivo.write("Título,Autor,Ano de publicação,Número de páginas\n")
    for i in range(10):
        titulo = input("Título: ")
        autor = input("Autor: ")
        ano_publicacao = input("Ano de publicação: ")
        numero_paginas = input("Número de páginas: ")
        
        livro = f"{titulo},{autor},{ano_publicacao},{numero_paginas}\n"
        arquivo.write(livro)
    arquivo.close