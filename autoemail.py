# CONFIGURAÇÕES INICIAIS:
#   - IMPORTAR smtplib PARA FUNCIONAR!
#   - pip instal smtplib NO SEU TERMINAL PYTHON

# AS OUTRAS BIBLIOTECAS POSSÍVELMENTE JÁ ESTÃO INSTALADAS NO SEU SISTEMA

import smtplib as obj
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime as dt
import os

hoster = 'smtp.gmail.com'
porta = 587
user = 'machinesdotcom@gmail.com'
senha = 'moctodsenihcam@2022'

######  DEFININDO O ENVIO DO EMAIL ######
def DefinirEmail() :
    global emailReceber
    global emailSubject
    global emailText
    emailReceber = input("Para qual email você deseja enviar? ")
    emailSubject = input("Assunto do Email: ")
    emailText = input("Texto do Email: (termine pressinando Enter): ")

######  CONEXÃO COM O SERVIDOR DE EMAIL ######
def ConectandoEmail():
    print('Criando objeto servidor...')
    server = obj.SMTP(hoster,porta)

    print('Logando na conta...')
    server.ehlo()
    server.starttls()
    server.login(user,senha)

    print('Criando o e-mail...')
    email_msg = MIMEMultipart()
    email_msg ['From'] = user
    email_msg ['To'] = emailReceber
    email_msg ['Subject'] = emailSubject

    print('Adicionando texto no email...')
    email_msg.attach(MIMEText(emailText, 'plain'))

    print('Enviando e-mail para o '+emailReceber+'...')
    server.sendmail (email_msg ['From'],email_msg ['To'], email_msg.as_string())

    print('Mensagem enviada com sucesso para ' + emailReceber)
    server.quit()

def IniciarEmail():
    DefinirEmail()
    horaDesejada = input("Qual hora programada para executar o email?")
    data = dt.now()
    hora = data.strftime('%H:%M')

    os.system('cls')
    print("AGUARDANDO PARA ENVIO")
    print("POR FAVOR NÃO FECHAR A TELA")
    print("------------------")
    print("Será enviado para: "+emailReceber)
    print("hora programada para envio: "+horaDesejada)

    while (horaDesejada != hora):
        data = dt.now()
        hora = data.strftime('%H:%M')
    
    if (horaDesejada == hora):
        ConectandoEmail()

IniciarEmail()
