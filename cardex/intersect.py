import os
os.chdir("c:/Python32/Scripts/cardex/")

def dates_intersect(date1, date2):
    verif1 = open(date1 + "/verificar.txt")
    verif2 = open(date2 + "/verificar.txt")
    cods1 = set(verif1.readlines())
    print(cods1.intersection(set(verif2.readlines())))
