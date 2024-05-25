horas_trabalhadas = [40, 37, 45, 40, 40, 48]
ganho_por_hora = 20
hora_extra = 25
pagamentos = [ganho_por_hora * min(i, 40) + hora_extra * max(0, i - 40) for i in horas_trabalhadas]
print(pagamentos)

