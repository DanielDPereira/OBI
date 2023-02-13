N = int(input())
ALP = input()

ALP_list = []
ALP_list.append(ALP.split(" "))
print(ALP_list)

A = int(ALP_list[0])
L = int(ALP_list[1])
P = int(ALP_list[2])

if A and L and P >= N:
    print("S")
else:
    print("N")
