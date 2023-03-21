N = int(input())

list = []
dias = 0
soma_acessos = 0

for i in range(N):
    list.append(int(input()))

while soma_acessos < 999999:
    soma_acessos = soma_acessos + list[dias]
    dias += 1
    
print(dias)