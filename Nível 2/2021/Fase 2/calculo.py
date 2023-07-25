S = int(input())

A = int(input())
B = int(input())

ListaIntervalo = []
Contador = A
while Contador <= B:
    ListaIntervalo.append(Contador)
    Contador+=1

#print(ListaIntervalo)

ListaNumerosNoIntervaloIguaisAS = []

for i in range(len(ListaIntervalo)):
    
    if len(str(ListaIntervalo[i])) == 1:
        if int(ListaIntervalo[i]) == S:
            ListaNumerosNoIntervaloIguaisAS.append(int(ListaIntervalo[i]))
    else:
        soma = 0
        for digito in str(ListaIntervalo[i]):
            soma += int(digito)
            
            if soma == S:
                ListaNumerosNoIntervaloIguaisAS.append(int(ListaIntervalo[i]))
        
            
#print(ListaNumerosNoIntervaloIguaisAS)
print(len(list(set((ListaNumerosNoIntervaloIguaisAS)))))
#print(len(ListaNumerosNoIntervaloIguaisAS))

    