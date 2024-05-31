<<<<<<< HEAD
def validador_senha(senha):
    if len(senha) <= 8:
        return False

    for letra in senha:
        if letra.isupper() == True:
            maiuscula = True

# isupper () e islower () e  isdigit



senha ='junior'
print(validador_senha(senha))
=======

def validador_senha(senha):

    if len(senha) < 8:
        return False
    
    contem_letra_maiuscula = False
    contem_letra_minuscula = False
    contem_numero = False
    contem_caractere_especial = False

    for i in senha:
        if i.isupper():
            contem_letra_maiuscula = True
        if i.islower():
            contem_letra_minuscula = True
        if i.isnumeric():
            contem_numero = True
        if i in "!@#$%^&*(),.?\":{}|<>":
            contem_caractere_especial = True

    return contem_letra_maiuscula and contem_letra_minuscula and contem_numero and contem_caractere_especial
 


senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"
print(validador_senha(senha1))
print(validador_senha(senha2))
print(validador_senha(senha3))
>>>>>>> 161bc23f071c362b82a5ea4afa4081895450fc7e
