
def ordenar_palavra(palavra):
    return sorted(palavra.lower())

def encontrar_anagramas(frase, palavra):
    anagramas = []
    for item in frase:
        if ordenar_palavra(item) == ordenar_palavra(palavra):
            anagramas.append(item)
    return anagramas


frase = input("Digite uma frase: ")
frase = frase.split()

palavra= input("Digite a palavra objetivo: ")

print(f"Anagramas: {encontrar_anagramas(frase, palavra)}")


