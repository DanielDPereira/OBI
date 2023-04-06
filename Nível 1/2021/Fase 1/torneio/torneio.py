X1 = input()
X2 = input()
X3 = input()
X4 = input()
X5 = input()
X6 = input()

listX = [X1, X2, X3, X4, X5, X6]

Y = listX.count("V")

if Y == 6:
    print("1")
elif Y == 5:
    print("1")
elif Y == 4:
    print("2")
elif Y == 3:
    print("2")
elif Y == 2:
    print("3")
elif Y == 1:
    print("1")
elif Y == 0:
    print("-1")