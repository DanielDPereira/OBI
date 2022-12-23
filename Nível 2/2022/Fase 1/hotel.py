#D = valor da diária
D = int(input())
#A = aumento
A = int(input())
#N = dia de chegada
N = int(input())

#Até o dia 15
if N<=15:
    preço = (32-N)*(D+(N-1)*A)

#Depois do dia 15
if N>15:
    preço = (32-N)*(D+A*14)

print(preço)
