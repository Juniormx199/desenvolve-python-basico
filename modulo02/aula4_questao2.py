#Entrada da temperatura em fahrenheit
fahrenheit = int(input("Informe a temperatura em fahrenheit:"))

#calculo da conversão de fahrenheit para celsius
celsius = (fahrenheit - 32) * (5/9)

#Mostrar informações para o usuario
print(f"{fahrenheit} graus Fahrenheit são {int(celsius)} graus Celsius.")