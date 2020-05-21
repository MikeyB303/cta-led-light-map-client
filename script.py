import socketio

sio = socketio.Client()

sio.connect('http://localhost:3000')

print('my sid is', sio.sid)


@sio.on('station-update')
def on_message(pixelDataArray):
    for pixelData in pixelDataArray:
        print(pixelData['isOn'])
