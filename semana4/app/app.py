# -*- coding: utf-8 -*-
"""Archivo principal para el echobot. Main File for the echobot"""
from fbmq import Page
from flask import Flask, request

# Token generado por la página web. Generated token in the facebook web page
PAGE_ACCESS_TOKEN = "EAACZAIynIJpoBAOOEpeXcDp92voZBXGQFxxp6ZA1wLed7VHKgtUo5srihqRHcZCVMSP2ypmwXkZBiklDacAUZCj3vM8ehJFSUlDg1kjxEatdI8dCFyr3A4mvUpEEYsX2IYzsiZCSIxicrlBDsJFbXPVROHH4a7wZAQRLhX0UdMbE8wDZAgocT7juy"
# Token generado por nosotros. Token generated by us
VERIFY_TOKEN = "EchoBotChido" # Si cambias este token, asegúrate de cambiarlo también en la página de configuración del webhook. If you change this token, verify that you changed it too in the webhook configuration.

app = Flask(__name__)
page = Page(PAGE_ACCESS_TOKEN) # Generamos la instancia de la página de facebook. We make the facebook page instance


@app.route('/')
def hello_world():
    """La página principal del servidor. The server main page."""
    return 'Inicio del servidor'


@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    """El método que se ejecuta cuando Facebook se conecta. This method executes as Facebook connect to us."""
    if request.method == 'POST':  # if the message is a POST, we handle it with message_handler. Si el mensaje es POST, se maneja con el message_handler
        # Facebook sends the user messages with a POST. Facebook manda los mensajes del usuario con un POST.
        page.handle_webhook(request.get_data(as_text=True))
        return 'ok'
    elif request.method == 'GET':  # if the message is a GET, we handle it here. Si el mensaje es un GET, lo manejamos aquí.
        # The first you configure the webhook, FB sends a GET to your webhook to verify that it really is you, and you're not working on someone's else page.
        # La primera vez que se configura el webhook, FB manda un mensaje GET para ver que realmente eres tú, y no estás trabajando en la página de alguien más.
        if request.args.get('hub.verify_token') == VERIFY_TOKEN:
            # If the verify token in the url matches our verify token we answer with the challenge to prove our identity.
            # Si el verify token de la url concuerda con el de nosotros le respondemos con el challenge o reto para verificar que somos nosotros
            return request.args.get('hub.challenge')
        return 'Wrong Verify token'


@page.handle_message
def message_handler(event):
    """Este método se ejecuta cuando nos llega un mensaje a la página. This method executes whenever a message is sent to our page."""
    # Se saca el id del sender. We get the sender id.
    sender_id = event.sender_id
    # Vemos si el mensaje es un texto o un adjunto (imagen, gif, sticker, etc)
    # We see if the message is a text or an attachment (image, GIF, sticker, etc)
    if event.is_text_message:
        # We get the message from the event variable and sent it back7
        # Obtenemos el mensaje de la variable event y se lo regresamos al usuario
        page.send(sender_id, "Hey, you send me: {}".format(event.message_text))
    elif event.is_attachment_message:
        page.send(sender_id, "Boo, you didn't send a text. ")


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True, threaded=True)