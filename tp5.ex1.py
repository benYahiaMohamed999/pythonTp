ch1="abc"
ch2="dc"
x1=set(ch1+ch2)
print(x1)

l2=[]
l1=[]
l3=[]
ch3=ch1+ch2
l1.append(ch3)
for i in range(len(l1)):
    for j in range(len(l1)):
        l2=l1[i]+l1[j]
for i in range(len(l2)-1):
    l3.extend([l2[i:i+2]])
chj=set(l3)
print(chj)
print(l2)