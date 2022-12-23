#Premiados
N = int(input())

#Array com tamanhos escolhidos
T = [int(i) for i in input().split()]

#Contando os escolhidos de cada tamanho
escolhidos1 = T.count(1)
escolhidos2 = T.count(2)

#Camisetas pequenas produzidas
P = int(input())

#Camisetas médias produzidas
M = int(input())



if P >= escolhidos1 and M >= escolhidos2:
    print("S")
else:
    print("N")

#By Daniel Dias Pereira