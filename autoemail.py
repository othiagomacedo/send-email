import smtplib as obj
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

hoster = 'smtp.gmail.com'
porta = 587
user = 'machinesdotcom@gmail.com'
senha = 'moctodsenihcam@2022'

print('Criando objeto servidor...')
server = obj.SMTP(hoster,porta)

print('Logando na conta...')
server.ehlo()
server.starttls()
server.login(user,senha)

mensagem = "Oi, este é um email automático enviado pelo Python"

print('Criando o e-mail...')
email_msg = MIMEMultipart()
email_msg ['From'] = user
email_msg ['To'] = 'thiagosoporcaria@gmail.com'
email_msg ['Subject'] = 'ESTE É UM EMAIL AUTOMÁTICO'

print('Adicionando texto no email...')
email_msg.attach(MIMEText(mensagem, 'plain'))

print('Enviando e-mail para o '+user+'...')
server.sendmail (email_msg ['From'],email_msg ['To'], email_msg.as_string())

print('Mensagem enviada com sucesso para ' + user)
server.quit()