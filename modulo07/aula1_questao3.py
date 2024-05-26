frase = input("Digite a frase: ")
espaco = 0
for i in frase:
    if i == " ":
        espaco += 1
    
print(f"Espaços em branco: {espaco}")