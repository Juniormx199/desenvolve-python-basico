def remove_pontuacao(cpf):
    numeros_cpf = ''
    for i in cpf:
        if i in "0123456789":
            numeros_cpf += i    
    return numeros_cpf

def encontra_digitos(cpf):
    digitos = ''
    for x in range(2):
        resultado = 0
        multiplicador = 10 + x
        for i in range(9 + x):
            resultado += int(cpf[i]) * multiplicador
            multiplicador -= 1
        resto = resultado % 11
        if resto >= 2:
            digitos += str(11 - resto)
        else:
            digitos += str(0) 
    return digitos

def verifica_digitos(cpf):
    cpf = remove_pontuacao(cpf)
    if len(cpf) == 11:
        digitos = encontra_digitos(cpf)
        if cpf[-2:] == digitos:
            print("CPF valido")
        else:
            print("CPF invalido")
    else:
        print("CPF precisa ter 11 digitos")


verifica_digitos(input("Digite o cpf: "))