import os
import shutil

#os.chdir('L:/Fotos com codigos')
#os.chdir('C:/Users/Heitor/Desktop/Fotos com codigos')
os.chdir('C:/Users/Heitor/Desktop/imagens')
categories = os.listdir('.')
for category in categories:
    os.chdir('C:/Users/Heitor/Desktop/imagens/' + category)
    for image in os.listdir('.'):
        if not image.endswith('.db'):
            print(category + image)
            shutil.copyfile('C:/Users/Heitor/Desktop/Fotos com codigos local/'+image, 'C:/Users/Heitor/Desktop/imagens/'+category+'/'+image)
