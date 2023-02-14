N = int(input())
ALP = input()

list = []

list.append(ALP.split(" "))

A = list[0][0]
L = list[0][1]
P = list[0][2]

A = int(A)
L = int(L)
P = int(P)
print("valor de A é  :", A)
print("valor de L é  :", L)
print("valor de P é  :", P)
if A <= N:
    if L <= N:
        if P <= N:
            print("S")
        else:
            print("N")
    else:
        print("N")
else:
    print("N")

input()