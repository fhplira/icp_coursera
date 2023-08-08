import math

x1 = float(input('Digite o valor de x1: '))
y1 = float(input('Digite o valor de y1: '))
x2 = float(input('Digite o valor de x2: '))
y2 = float(input('Digite o valor de y2: '))

dx = (x1 - x2) ** 2
dy = (y1 - y2) ** 2

distancia = math.sqrt(dx + dy)

if distancia >= 10:
    print('longe')
else:
    print('perto')
