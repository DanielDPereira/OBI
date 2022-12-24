N = int(input())

list_1 = []

for i in range(N):
    T = input()
    #T é o valor sem formatação

    X = len(T)-1
    #X é a quantidade de caracteres do número

    Y = T[X]
    #Y é o último digito

    N = T[:-1]
    #N é o número exceto o útimo digito

    M = int(N)**int(Y)

    list_1.append(M)

print(sum(list_1))

#By Daniel Dias Pereira