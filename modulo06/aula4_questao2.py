

frase = input("Digite uma frase: ")
vogais = [i for i in frase if i.lower() in ["a","e","i","o","u"]]
consoantes = [i for i in frase if i.lower() not in ["a","e","i","o","u"," "]]

print(f"Vogais: {vogais}")
print(f"Consoantes: {consoantes}")