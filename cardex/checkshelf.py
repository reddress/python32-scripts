import shelve

SHELF_FILE = "c:/Python32/Scripts/cardex/codshelf"

codshelf = shelve.open(SHELF_FILE)

for key in sorted(codshelf.keys()):
    print("%s : %s" % (key, codshelf[key]))

