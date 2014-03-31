import smtplib

from_addr = 'heitorpontual@gmail.com'
to_addr = 'heitorchang@gmail.com'
subj = 'URGENT heitor VERY IMPORTANT MAKE $$$ NOW'
msg = 'This is spam from Gmail through a Python script'

username = 'heitorpontual'
password = '123abc!@#'
message = "From: " + from_addr + "\nTo: " + to_addr + "\nSubject: " + subj + "\n\n" + msg

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to_addr, message)
server.quit()
