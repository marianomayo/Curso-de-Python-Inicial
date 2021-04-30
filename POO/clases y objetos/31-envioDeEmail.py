#!/usr/bin/python
# -*- coding: utf-8 -*-

#Enviar correo Gmail con Phython

import smtplib

remitente = 'marianoagustinmayo@gmail.com'
destinatario = 'marianoagustinmayo@gmail.com'
msg = 'Correo enviado utilizando Phyton'

#Datos
username = 'marianoagustinmayo@gmail.com'
password = ''

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(remitente, destinatario, msg)
server.quit()