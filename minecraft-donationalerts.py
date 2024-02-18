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

    def on_command():
        if (float(amount) % 10 == 0):
            give = 'give '
            number = float(amount) / 10
            numberInt = int(number)
            name = username
            object = ' minecraft:diamond '
            command = give + name + object + str(numberInt)
            return command
        else:
            print('false')

        return on_command()

    mc.connect()
    mc.command(on_command())


sio.connect('wss://socket.donationalerts.ru:443', transports='websocket')
