import smtplib as smtp
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
msg = MIMEMultipart()
texto = "Estou enviando um email com Python"

#parâmetros
senha = "SUA SENHA"
msg['From'] = "SEU E-MAIL"
msg['To'] = "E-MAIL DESTINO"
msg['Subject'] = "ASSUNTO"

msg.attach(MIMEText(texto, 'plain'))
server = smtp.SMTP('smtp.gmail.com: 587')
server.starttls()

server.login(msg['From'], senha)


server.sendmail(msg['From'], msg['To'], msg.as_string())


server.quit()

print('Mensagem enviada com sucesso')