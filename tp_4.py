

t=[]
t2=[]
nb=0
nombImp=0
n=int(input("donner n :"))
i=0
j=1
somme=0
for i in range(n):
    a=int(input())
    t.append(a)
    print(i,"son contune est :",t[i]) 
print("le somme:",sum(t))
print("min:",min(t))
print("max:",max(t))
for i in range(n):
   
    if(t[i]%2==0):
        nb+=1
        
    else:
        nombImp+=1
for i in t:
    t2.append(i*3)
print("nombre paire :",nb)
print("nombre impaire:",nombImp)
print("le tab Mult 3 ==>",t2)

    

