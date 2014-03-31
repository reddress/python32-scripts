import shelve

# folder = input("Enter directory name (date): ").strip()

def update(folder):
    SHELF_FILE = "c:/Python32/Scripts/cardex/codshelf"
    codshelf = shelve.open(SHELF_FILE)
    
    try:
        with open("c:/Python32/Scripts/cardex/" + folder + "/verificar.txt") as verif:
            for line in verif:
                # print("'%s'" % line)
                codshelf[line.strip()] = folder
            
    except FileNotFoundError:
        print("Directory does not exist.")
    
    finally:
        codshelf.close()

update("2014_01_17")
update("2014_01_20")
update("2014_01_23")
