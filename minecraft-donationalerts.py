import socketio
import json
from mcrcon import MCRcon
from config import token, ip, password, port

TOKEN = token
mc = MCRcon(ip, password, port = port)
sio = socketio.Client()

@sio.on('connect')
def on_connect():
    sio.emit('add-user', {"token": TOKEN, "type": "alert_widget"})

@sio.on('donation')
def on_message(data):
    y = json.loads(data)
    username = y['username']
    amount = y['amount']
    currency = y['currency']
    message = y['message']

    if (float(amount) % 10 == 0):
        mc.connect()
        give = 'give '
        number = float(amount) / 10
        numberInt = int(number)
        name = username
        object = ' minecraft:diamond '
        print(give + name + object + str(numberInt))
        mc.command(give + name + object + str(numberInt))  ## Для примера алмаз
    else:
        print('false')

sio.connect('wss://socket.donationalerts.ru:443', transports='websocket')