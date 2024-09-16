import websocket
import json

def on_open(ws):
    print("Conectado al WebSocket")
    ws.send(json.dumps({'message': 'Hola, servidor!'}))

def on_message(ws, message):
    data = json.loads(message)
    print("Mensaje del servidor:", data['message'])

def on_error(ws, error):
    print("Error en la conexión WebSocket:", error)

def on_close(ws):
    print("Desconectado del WebSocket")

if __name__ == "__main__":
    ws = websocket.WebSocketApp(
        "ws://localhost:8000/ws/recognition/",
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    ws.run_forever()
