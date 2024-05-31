def validador_senha(senha):
    if len(senha) <= 8:
        return False

    for letra in senha:
        if letra.isupper() == True:
            maiuscula = True

# isupper () e islower () e  isdigit



senha ='junior'
print(validador_senha(senha))