N = int(input())
sequencia = input()

sequencia_list = sequencia.split(" ")

X = 0

for i in range(len(sequencia_list)-2):    
    if sequencia_list[i] == "1":
        if sequencia_list[i+1] == "0":
            if sequencia_list[i+2] == "0":
                X = X + 1
    
print(sequencia_list)
print(X)