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

if A and L and P < N:
    print("S")
else:
    print("N")
