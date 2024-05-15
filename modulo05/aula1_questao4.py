from datetime import datetime

agora = datetime.now()

data_atual = agora.date()
hora_atual = agora.time()



print("Data atual:", data_atual.strftime('%d/%m/%Y'))
print("Hora atual:", hora_atual.strftime('%H:%M:%S'))