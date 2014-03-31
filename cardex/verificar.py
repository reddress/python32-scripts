import os
import re
import shutil
import shelve

SHELF_FILE = "c:/Python32/Scripts/cardex/codshelf"

codshelf = shelve.open(SHELF_FILE)

def remove_txt(s):
    m = re.match(r'(?P<cont>\w+)', s)
    if m.group('cont') == 'semcont':
        return "#"
    else:
        return m.group('cont')

# print(os.getcwd())
date = input("Enter directory name (date): ").strip()
counter = 1
try:
    #print("C:/Users/Heitor/PycharmProjects/cardex/" + date)
    #os.chdir("C:/Users/Heitor/PycharmProjects/cardex/" + date)
    os.chdir("c:/Python32/Scripts/cardex/" + date)
    v_list = []
    with open('verificar.txt') as v:
        for line in v:
            v_list.append(line.strip().upper())

    with open('sorted.txt', mode='w') as s:
        for cod in sorted(list(set(v_list))):
            # prune codigos here
#            ask = input("(Enter to keep, 'x' to remove) Last seen %s, %s? " % (codshelf.get(cod, "====/-n/a-"), cod))
#            if len(ask) > 0:
#                print("removing", cod)
#            else:
#                print(cod, file=s)
            print(cod, file=s)
            # set new codigo date
#            codshelf[cod] = date

    print()
    print(" ======================== QUANTITY ============================= ")
    print()
            
    all_files = set(os.listdir())
    lst = os.listdir()

    container = {}
    for c_filename in all_files:
        container[c_filename] = set()
        with open(c_filename) as f:
            for line in f:
                container[c_filename].add(line.strip().upper())

    with open('sorted.txt') as v:
        with open('sortedautoit.txt', mode='w') as sortau:
            with open('lista.csv', mode='w') as lista:
                for prod_full in v:
                    prod = prod_full.strip()
                    vaiChegar = False
                    print(prod, file=lista, end="")
                    print(prod, file=sortau, end="")
                    for c_filename in all_files:
                        if c_filename[-1] == "~" or c_filename == 'verificar.txt' or c_filename == 'sryehtotal.txt' or c_filename == 'sorted.txt' or c_filename == 'sortedautoit.txt' or c_filename == 'lista.csv':
                            pass
                        else:
                            with open(c_filename) as c:
                                if prod in container[c_filename]:
                                    #print("(%d) %s - %s" % (counter, prod, c_filename))
                                    qtd = input("last seen %s, qty for %s (%s) " % (codshelf.get(prod, "now"), prod, remove_txt(c_filename)))
                                    print(",%s (%s)" % (qtd, remove_txt(c_filename)), file=lista, end="")
                                    if not vaiChegar:
                                        print("@", file=sortau, end="")
                                    else:
                                        print("/", file=sortau, end="")
                                    print("%s (%s)" % (qtd, remove_txt(c_filename)[-2:]), file=sortau, end="")
                                    vaiChegar = True
                    print("", file=lista)
                    print("", file=sortau)
                    codshelf[prod] = date
                    counter += 1
    print(os.getcwd())
    shutil.copyfile('lista.csv', 'D:/pontual/Cardex/' + date + '_lista.csv')
    print("Copied to D:/pontual/Cardex/" + date + '_lista.csv')

    shutil.copyfile('sortedautoit.txt', 'C:/Users/Heitor/Desktop/install Autoit/Scripts/sortedautoit.txt')
    print("Copied sortedautoit.txt to C: autoit")
    print("******")
    print("ALL OK")
except Exception as E:
    print(E)
    #print("Directory/File does not exist.")
finally:
    codshelf.close()
