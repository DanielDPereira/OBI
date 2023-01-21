D = int(input())
A = int(input())
N = int(input())

res = (32 - N) * (D + A * (min(N - 1, 14)))

print(str(res))
