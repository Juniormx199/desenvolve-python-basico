meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

data_nascimento = input("Digite uma data de nascimento: ").split("/")

mes_nascimento = int(data_nascimento[1])

print(f"Você nasceu em  {data_nascimento[0]} de {meses[mes_nascimento - 1]} de {data_nascimento[2]}.")