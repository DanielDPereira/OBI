#consumo do carro em km/l
C = int(input())

#distância do aeroporto em km
D = int(input())

#litros antes do abastecimento
T = int(input())

x = D / C - T
y = float(x)

#resultado

if x > 0:
    print(round(y, 1))

if x <= 0:
    print(float(0))