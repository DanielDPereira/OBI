N = int(input())

list=[]

for i in range(N):
    X = int(input())

    if X != 0:
        list.append(X)

    if X == 0:
        list.pop()

print(sum(list))

#By Daniel Dias Pereira