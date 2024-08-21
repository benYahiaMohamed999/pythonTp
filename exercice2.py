t=[]
n=int(input("donner n"))
for i in range(n):
    print("son contune est :") 
    a=int(input())
    t.append(a)
print("My Table::>>>",t)
for i in t:
    if(t.count(i)>1):
        t.remove(i)
print("New Tab:",t)
