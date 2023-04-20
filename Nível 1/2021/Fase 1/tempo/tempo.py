N = int(input())
lista = []
leitura = []

for x in range(N):
    leitura = []
    leitura = list(input().split())
    if x == 0:
        leitura.append(0)
    elif lista[x-1][0] != "T":
        if leitura[0] != "T":
            leitura.append(1)
    else:
        leitura.append(lista[x-1][1])
        
    lista.append(leitura)
    
tempo = []
terminou = []

for y in range(N):
    if lista[y][0] == "R" and lista[y][1]:
        tempo[int(lista[x][1])] = 0
        
    