numero = input("Digite o número:")
if len(numero) == 8:
    numero_completo = "9"+numero[:4]+"-"+numero[4:]
elif len(numero) == 9:
    numero_completo = numero[:5]+"-"+numero[5:]
else:
    numero_completo = "Numero invalido"
    
print(numero_completo)