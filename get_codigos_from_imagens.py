import os

codigos = []

os.chdir('C:/Users/Heitor/Desktop/imagens')
categories = os.listdir('.')
for category in categories:
    os.chdir('C:/Users/Heitor/Desktop/imagens/' + category)
    for image in os.listdir('.'):
        if not image.endswith('.db'):
            codigos.append(image[0:-4])

# remove duplicates
codigos_set = set(codigos)

codigos = list(codigos_set)
codigos.sort()

output = open('C:/Python32/Scripts/codigos_from_imagens.txt', mode='w')
for codigo in codigos:
    print(codigo, file=output)

output.close()
