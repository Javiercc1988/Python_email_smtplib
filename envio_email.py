import csv,smtplib, ssl
import getpass


# 1. Declaramos las variables fijas, mensaje, puerto, email desde que se envia
# y ocultamos la password para cuando lo pongamos no se vea la contraseña en consola

web = "http://localhost:15200"

mensaje = """Subject: {}

Hola! {}, te escribo para decirte que: {}, y mi direccion web {}"""

destinatario = 0
port = 465
sender = "example1@example.com"
password = getpass.getpass('Password:')

# Creamos la conexión segura por SSL
context = ssl.create_default_context()


#2. Creamos la conexión SMTP
#Conexion SMTP al dominio smtp.gmail.com
with smtplib.SMTP_SSL("smtp.gmail.com",port, context=context) as s:
    destinatario += 1
    s.login(sender, password)
    #3. Abrimos y leemos el fichero
    with open("direcciones_y_texto.csv") as file: # Abrimos el archivo csv
        reader = csv.reader(file) # Usamos el metodo reader de csv
        next(reader) # Omitimos la primera linea que es la cabecera

        #4. Recorremos el fichero linea por linea
        for name, email, texto in reader: # Leemos los 3 valores por linea
            s.sendmail(sender,
                       email,
                       mensaje.format(name,name,texto,web))
            print("Enviado email a {}".format(name))
