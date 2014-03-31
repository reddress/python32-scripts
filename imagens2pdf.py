import os

os.chdir('C:/Users/Heitor/Desktop/imagens_pdf_cc')
categories = os.listdir('.')

for category in categories:
    os.chdir('C:/Users/Heitor/Desktop/imagens_pdf_cc/' + category)
    #print(os.listdir('.'))
    img_count = 0
    with open(category + ".html", mode="w") as html:
        print("""
<html>
<head>
<style>
body { position: relative; font-family: Arial, sans-serif; }
p { page-break-inside: avoid;
position: relative;
}
</style>
</head>
<body>
<p>
Pontual Exportação e Importação Ltda. (11) 3312-8845<br><b>É necessário consultar o estoque antes de fechar algum pedido.
<br>Preços sujeitos a alterações.</b>
<table><tr><td></td>
""", file=html)

        for file in os.listdir('.'):
            if file.lower().endswith('.jpg') and file[0:2] == 'cc':
                if img_count % 2 == 0:
                    print('</tr></table><hr><table border="0"><tr>', file=html)
                print('<td><img src="' + file + '"><br><center><b>' + file[3:-4] + '</b></center></td>', file=html)
                img_count += 1
        print("</body></html>", file=html)
    print(category + ": " + str(img_count))
    
