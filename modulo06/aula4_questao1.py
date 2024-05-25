
pares = [i for i in range(20,52,2)]
print(f"Números pares entre 20 e 50: {pares} \n")

quadrados = [i**2 for i in range(1,10)]
print(f"Quadrados de 1 a 9: {quadrados} \n")

divisiveis = [i for i in range(1,101) if (i % 7) == 0 ]
print(f"Números entre 1 e 100 divisíveis por 7 : {divisiveis} \n")

par_impar = [ "Par" if (i % 2) == 0 else "Impar" for i in range(0,30,3)]
print(f"Par ou impar de 0 a 30 pulo 3: {par_impar}")
