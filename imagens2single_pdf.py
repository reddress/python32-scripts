import os

os.chdir('C:/Users/Heitor/Desktop/imagens_pdf')
categories = os.listdir('.')

with open("singlePdf.html", mode="w") as html:
    print("""
<html>
<head>
<style>
body { position: relative; font-family: Arial, sans-serif; }
table { page-break-inside: avoid;
position: relative;
}
</style>
</head>
<body>
<p>
Pontual Exportação e Importação Ltda. (11) 3312-8845<br><b>É necessário consultar o estoque antes de fechar algum pedido.
<table><tr><td></td>
""", file=html)

    for category in categories:
        #print("<b>" + category + "</b>", file=html)
        os.chdir('C:/Users/Heitor/Desktop/imagens_pdf/' + category)
        #print(os.listdir('.'))
        img_count = 0

        for file in os.listdir('.'):
            if file.lower().endswith('.jpg') and file[0:4] == 'mini':
                if img_count % 3 == 0:
                    print('</tr></table><hr><table border="0"><tr>', file=html)
                print('<td><img src="' + category + "/" + file + '"><br><center><b>' + file[8:-4] + '</b></center></td>', file=html)
                img_count += 1
        print("</body></html>", file=html)
    print(category + ": " + str(img_count))
    
