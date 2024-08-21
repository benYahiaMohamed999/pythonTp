while True:
    mp=input("donner mdp :")
    if(len(mp)<=10 and (mp.find("A")!=-1 or mp.find("a")!=-1) and mp.find(" ")==-1):
        print("thnks For this password")
        break
    else:
        print( None)

print(mp.upper)
