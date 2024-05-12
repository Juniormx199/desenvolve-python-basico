classe  = input("Escolha a classe (guerreiro, mago ou arqueiro): ")
forca = int(input("Digite os pontos de força (de 1 a 20): "))
magia = int(input("Digite os pontos de magia (de 1 a 20): "))
valido = (( (classe.lower() == "guerreiro") and (forca >= 15 and forca <= 20) and (magia <= 10) )
or
( (classe.lower() == "mago") and (forca <= 10) and (magia >= 15 and magia <= 20) )
or
( (classe.lower() == "arqueiro") and (forca > 5 and forca <= 15) and (magia > 5 and magia <= 15) )
)

print("Pontos de atributo consistentes com a classe escolhida: ",valido)