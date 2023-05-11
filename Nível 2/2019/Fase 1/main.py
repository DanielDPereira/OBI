M = int(input())
A = int(input())
B = int(input())

X = M - (A + B)

list = [M, A, B, X]
list.sort()

print(list[2])