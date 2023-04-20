n = int( input() )  #leitura do número de eventos
eventos = [] #zera lista
tempos = [] #zera listas

if n >= 1 and n <=20: #verifica restrição
    for x in range(n): #leitura dos eventos (recebido, enviado ou tempo)
        leitura = [] #zera lista
        leitura = list(input().split()) #leitura da linha com n colunas
        leitura[1] = int(leitura[1]) #forçando a conversão do tipo string para inteiro (amigo)

        if leitura[1] >= 1 and leitura[1] <= 100: #verifica restrição

            if x == 0: #se for a primeira linha então inclui o tempo 0
                leitura.append(0)
            elif eventos[x-1][0] != 'T' :  #se a linha anterior for diferente de T
                if leitura[0] != 'T' : #se a linha atual for diferente de T então adiciona o tempo 1
                    leitura.append(1)
                else: #senão adiciona 0
                    leitura.append(0)
            else: #linha anterior é igual a T e adiciona o tempo passado entre os eventos
                leitura.append( eventos[x-1][1] )

            eventos.append(leitura) #adiciona o evento na lista

            if leitura[0] == 'R': #se linha for R então inclui um item na lista de tempos
                item = [leitura[1], 0, -1]  
                if tempos.count(item) == 0:  #se o item não existir na lista de tempos então adiciona
                    tempos.append(item)

    total = len(tempos)
    for y in range(total): #calcula o tempo entre o evento recebido e o evento enviado
        for x in range(n):
            item = eventos[x]
            if eventos[x][0] == 'R' and item[1] == tempos[y][0]: #se for R e for o amigo então zera soma
                soma = 0
                tempos[y][2] = -1
            if eventos[x][0] == 'R' and item[1] != tempos[y][0]: #se for R e não for o amigo então soma tempo
                soma = soma + item[2]
            if eventos[x][0] == 'E' and item[1] != tempos[y][0]: #se for E e não for o amigo então soma tempo
                soma = soma + item[2]
            if eventos[x][0] == 'E' and item[1] == tempos[y][0]: #se for E e for amigo então grava a soma
                soma = soma + item[2]
                tempos[y][1] = tempos[y][1] + soma #acumula as somas
                tempos[y][2] = 0
   
    for x in range(total):
      if tempos[x][2] == -1: #se não enviou a mensagem então será -1
          tempos[x][1] = -1
      print( tempos[x][0], tempos[x][1] ) #imprime o resultado