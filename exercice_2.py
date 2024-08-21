ch = input("saisissez votre text : ")

ch2 = {}
for i in ch:
    if i not in ch2:
        ch2[i] = 1
    else:
        ch2[i] += 1

print(ch2)