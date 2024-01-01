from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviar_correo', methods=['POST'])
def enviar_correo():
    nombre = request.form['nombre']
    email = request.form['email']
    mensaje = request.form['mensaje']

    # Configurar el servidor SMTP
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_user = 'alejandro.lopez14591@gmail.com'
    smtp_password = 'ciroalejandroliamsebastian1'

    # Crear el mensaje
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = 'tufyalmafuerte2@gmail.com'
    msg['Subject'] = 'Nuevo mensaje de contacto desde el formulario'

    body = f'Nombre: {nombre}\nEmail: {email}\nMensaje: {mensaje}'
    msg.attach(MIMEText(body, 'plain'))

    # Enviar el correo
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.send_message(msg)

    return 'Mensaje enviado correctamente'

if __name__ == '__main__':
    app.run(debug=True)