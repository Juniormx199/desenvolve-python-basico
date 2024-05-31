 
vogais = ["a","e","i","o","u"]

frase = input("Digite uma frase: ").lower()
for i in range(5):
    frase = frase.replace(vogais[i] , "*")

print(f"Frase modificada: {frase}")