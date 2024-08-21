mdp=input("donner password")

t=['!','@','#','$','%']
if len(mdp)<8:
    print("error doive plus de 8 charcter")

for i in mdp:
    if not(i.isupper and i.islower):
        print("error majus minus")
for i in mdp:
    test=True
    if not(i.isdigit==test):
        if test==False:
            print("error in number")

for i in mdp:
    test==i in t
    if test==True:
        print("sibon")
    else :
        print("il faux entry des symbole")
        break

