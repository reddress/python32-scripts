import os

os.chdir("C:/users/heitor/Desktop/fotos com codigos local")

ls = os.listdir()

os.chdir("C:/users/heitor/Desktop/")

with open("codigos.txt", mode="w") as o:
    for item in ls:
        print('"' + item[0:-4] + '",', file=o)

        
