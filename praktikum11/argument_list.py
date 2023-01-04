#def sumAll(angka1, angka2, angka3, angka4,):
#    total = angka1 + angka2 + angka3 +angka4
#    print(total)


#sumAll(2,4,5,7)

def sumAll(*values):
    total = 0
    for i in values:
        total += i
    print(total)
    
sumAll(2,4,5,7,6,7,8,8,8)