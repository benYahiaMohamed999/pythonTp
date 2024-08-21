from random import randint

def ex1():
    s=0
    for i in range(8):
        x=int(input("donner x"))
        while(x%2!=0):
             x=int(input("donner x"))
        if(x>0):
            s=s+x
        else:
            print(s)
            break
    print(s)
                
                
        
    
def ex2():
    for i in range(9):
        for j in range(9):
            print(i,"*",j,"=",i*j)


def ex3():
    x=int(input("donner nombre positif "))
    while(x<0):
         x=int(input("donner nombre positif "))
    for i in range(1,x):
        if(x%i==0 and i!=1):
            print(x,"est sont devisuer :",i)
        else:
            print("aucun ! il Premier")


def ex4():
    n=randint(1,30)
    for i in range(5):
        x=int(input("doner essai"))
        if(x<n):
            print("plus petit")
        elif(x>n):
            print("trop grand")
        else:
            print("le bonne repose")
    print("le repose est ",n)



def exSupp2():
    x="*"
    l=int(input("L:"))
    for i in range(l,0,-1):
        print(x*i)
       
       
            

def exSupp1():
    
    l=int(input("L:"))
    for i in range(1,l+1):
        x=""
        while(len(x)<l-i):
            x=x+" "
        while(len(x)<l):
            x=x+"*"
        print(x)
       
                  
exSupp2()