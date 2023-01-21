X = int(input())
N = int(input())

Gastos = []

for i in range(N):
    Gastos.append(int(input()))

Quota = X * (N+1)

resultado = Quota - sum(Gastos)

print(resultado)

#By Daniel Dias Pereira
