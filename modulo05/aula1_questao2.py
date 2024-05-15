import random
import math

n = int(input("Valor: "))
total = 0

for i in range(n):
    total += random.randint(0 , 100)

print(math.sqrt(total))
