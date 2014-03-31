import os
import shutil

codigos = []

sem_imagens = "C:/Users/Heitor/Desktop/Fotos-sc/"

os.chdir('C:/Users/Heitor/Desktop/imagens_pdf')

categories = os.listdir('.')
for category in categories:
    os.chdir('C:/Users/Heitor/Desktop/imagens_pdf/' + category)
    for filename in os.listdir('.'):
        if filename.lower().endswith('.jpg') and not filename[0:2] == "sc":
            try:
                shutil.copyfile(sem_imagens + filename, "sc_" + filename)
            except IOError:
                print("Warning: " + filename + " not found")
                shutil.copyfile(filename, "sc_" + filename)
