##
## WARNING: RUN ONLY INSIDE CMD OR BASH
##

import os
import shutil

os.chdir('C:/Users/Heitor/Desktop/imagens_pdf_cc')

categories = os.listdir('.')
for category in categories:
    os.chdir('C:/Users/Heitor/Desktop/imagens_pdf_cc/' + category)
    for filename in os.listdir('.'):
        if filename.lower().endswith('.jpg'):
            print("Now processing: " + category + "/" + filename)
            try:
                os.system("convert " + filename + " -resize 320x cc_" + filename)
            except IOError:
                print("Warning: " + filename + " not converted")
