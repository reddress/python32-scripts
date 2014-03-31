from __future__ import print_function

from collections import defaultdict

import os
import shutil
import odf2array as odsreader

os.chdir("c:/Python32/Scripts/cardex/")

workdir = raw_input(r"Enter directory name under c:\Python32\Scripts\cardex: ")

try:
    os.chdir(workdir)

    CHEGANDO = odsreader.ODSReader("N:/CHEGANDO.ods")
    chegandotable = CHEGANDO.getSheet("Planilha1")
    
    sortedautoit = open("sortedautoit.txt", "w")
    verificar = open("verificar.txt")

    # read amounts from CHEGANDO
    chegaporcodigo = defaultdict(str)
    
    for row in chegandotable[1:]:
        codigo, container, chegando = row[1:]
        chegaporcodigo[codigo] += "%s (%s) " % (chegando, container[2:])

    # read sryeh.txt if it exists
    try:
        sryeh = open("sryeh.txt")
        for raw_line in sryeh:
            codigo = raw_line.strip()
            chegaporcodigo[codigo] += "? (SrY)"
    except IOError, WindowsError:
        print("Sr. Yeh .txt not found.")
    
    # read verificar
    veriflines = verificar.readlines()
    veriflines = list(set(veriflines))
    veriflines.sort()
    
    for line in veriflines:
        codigo = line.strip()
        print("%s@%s" % (codigo, chegaporcodigo[codigo]), file=sortedautoit)

    verificar.close()
    sortedautoit.close()
    
    shutil.copyfile('sortedautoit.txt', 'C:/Users/Heitor/Desktop/install Autoit/Scripts/sortedautoit.txt')
    
    dummy = raw_input("Press Enter to quit. ")
except IOError, WindowsError:
    print("Directory does not exist. Create it and enter verificar.txt in it.")
