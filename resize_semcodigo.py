##
## WARNING: RUN ONLY INSIDE CMD OR BASH
##

import os
import shutil

os.chdir('C:/Users/Heitor/Desktop/imagens_pdf')

categories = os.listdir('.')
for category in categories:
    os.chdir('C:/Users/Heitor/Desktop/imagens_pdf/' + category)
    for filename in os.listdir('.'):
        if filename.lower().endswith('.jpg') and filename[0:2] == "sc":
            print("Now processing: " + category + "/" + filename)
            try:
                os.system("convert " + filename + " -resize 320x peq_" + filename)
            except IOError:
                print("Warning: " + filename + " not converted")
