
frase = input("Digite uma frase: ")
vogais = 0
indices = []

for i in range(len(frase)):
    if frase[i] in "aeiou":
        vogais += 1
        indices.append(i)

print(f"{vogais} vogais")
print(f"Índices {indices}")