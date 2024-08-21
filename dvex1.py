list1=[("a",1),("b",2),("c",3)]
list2=[("b",1),("c",2),("d",3)]
list3=set(list1+list2)
val=0
t=()
for key,value in list3:
    print(key,value)
    if key == 'b':
        val=value
        print(val)
        
    elif key == "c":
        valc=value
        
    elif key == "d":
        vald=value

    t.(key,val)
    t.insert(key,valc)
    t.insert(key,vald)
print(t)

