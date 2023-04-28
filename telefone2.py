P = input()

list = []

for i in range(len(P)):
    if P[i] == "A" or P[i] == "B" or P[i] == "C":
        list.append("2")
    if P[i] == "D" or P[i] == "E" or P[i] == "F":
        list.append("3")
    if P[i] == "G" or P[i] == "H" or P[i] == "I":
        list.append("4")
    if P[i] == "J" or P[i] == "K" or P[i] == "L":
        list.append("5")
    if P[i] == "M" or P[i] == "N" or P[i] == "O":
        list.append("6")
    if P[i] == "P" or P[i] == "Q" or P[i] == "R" or P[i] == "S":
        list.append("7")
    if P[i] == "T" or P[i] == "U" or P[i] == "V":
        list.append("8")
    if P[i] == "W" or P[i] == "X" or P[i] == "Y":
        list.append("9")
    if P[i] == "-":
        list.append("-")
x = ""

for i in range(len(list)):
    x = x + list[i]
    
print(x)