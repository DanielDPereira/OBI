#Ainda não está 100/100

N = int(input())
N2 = input()
N2.split(" ")

x = 0

A = "0"
B = "0"

def interroputor_I1():
    if A == "0":
        A = "1"
    
    if A == "1":
        A = "0"
        
def interroputor_I2():
    if A == "0":
        A = "1"
        
    if A == "1":
        A = "0"
        
    if B == "0":
        B = "1"
        
    if B == "1":
        B = "0"

for i in range(N):
    x = N2[i]
    
    if x == "1":
        interroputor_I1()
        
    if x == "2":
        interroputor_I2()
        
#prints
if A == "1":
    print("1")
else:
    print("0")
    
if B == "1":
    print("1")
else:
    print("0")
