genero = input("Informe seu gênero (M ou F): ")
idade = int(input("Informe sua idade: "))
tempo = int(input("Informe seu tempo de serviço (em anos): "))
apto = ((genero.lower() == "f" and  idade > 60 )
        or
        (genero.lower() == "m" and  idade > 65 )
        or
        (tempo >= 30)
        or
        (idade >= 60 and tempo >= 25)
        ) 
print("Apto para se aposentar: " , apto)

