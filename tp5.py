Notes={"ali":[8,10,5],
       "Mohamed":[12,10,17],
       "Asma":[12,10,17],
       "Aicha":[12,10,17],
       }

etudianadmi={}
etudiantNo={}
for cle,valeur in Notes.items():
    Notes[cle]=(valeur[0]+valeur[1]+valeur[2])/3

for cle,valeur in Notes.items():
    if(Notes[cle]>=10):
        print("/////////",cle,valeur)
        etudianadmi[cle]=valeur
    else:
        etudiantNo[cle]=valeur



print(Notes)
print(etudianadmi)
print(etudiantNo)
print("le nom de maxumaum note::>",max(etudianadmi))

