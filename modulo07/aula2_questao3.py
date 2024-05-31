
def remove_especiais(frase):
    return ''.join(e for e in frase if e.isalnum()).lower()

while True:
    frase = input("Digite uma frase (digite 'fim' para encerrar): ")

    if frase.lower() == "fim": break

    frase_modificada = remove_especiais(frase)

    if frase_modificada[::-1] == frase_modificada[::1]:
        print(f"'{frase}' é palíndromo")
    else:
        print(f"'{frase}' não é palíndromo")
