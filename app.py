# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", name="Flask")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

#readgs.py
import gspread
gc = gspread.service_account(filename='credentials.json')

# Abrir por titulo
sh = gc.open("Indexacion proyectos")

# Seleccionar primera hoja
worksheet = sh.get_worksheet(0)

# Introducir datos
worksheet.update('A1', 'dominio')
worksheet.update('A2', 'scraping.link')
worksheet.update('B1', 'fecha')
worksheet.update('B2', '22/04/2021')
worksheet.update('C1', 'num URLs indexadas')
worksheet.update('C2', '10')

{
  "type": "service_account",
  "project_id": "probable-axon-402219",
  "private_key_id": "c803c813b97c9894a7f6d356a5b5e3bc4efdaacf",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDaqXITu3VPSzKh\n5jS0j/Wm2rucaK/TtGLaYuCy4Fr+ZMnnd7smZTVxLWgCUFF9H4Bh2irAThr+V/z5\nC29FGUG54Et3QRJoslJ++9k27AD5Vhc/f2oKCag6W2UUD9QvEgjQbL8bSEsPh/+s\nwofmrfhp/r+6gg47n3IEvk7hQb1joXng7yyd7opZxiUA0YfRxVmbyMIi2wMXCCYj\n6GfgRjfb8ZW4t6rGY9pN6e7KtJ946hiIrpgEYNEwJZ0jbvzjJacItZEGD4nz01bs\nYoL6Sk6tfWs0kXtjSfdFOl3e1MASrGRIUrcm0Fb2w6byDOuMA3/qlpKt8AhdVB8u\neNYdyPqXAgMBAAECggEABpd8beXad8/PhfFCU33SLPvZE10AjUREhUrdH+dYNuUO\nRSER45Vs0q2eE2Zyc8WDAZrUa8RZrKM1vW2VJs3Hx8pgMVx6fpd+7ym5IZ5kZR/Y\nRuduE0Fj8JEYGfkO2iBpYvHJomaVL1xX3nsQImnKMap8Ayuv3CecBf1ACYBe15BU\nrkSN3Vz8tBoDmGCCtjOSk4VO1BfiVJnW0+7QXb/P880GRcKb4/ppnV3m9ga+q5um\nkPcq/3foTzJIoPyTvd6GU8QvhBBpfl+FLjXa5/2jFU8ovWD+YZ0FOqLuHBSvKFkk\n6y7aOQEmkLx+G/po5HEzSzf0p9RdvIQqTVASH/s0MQKBgQD0NhDuTw4BjL29N6Rk\nikUmLbkQYfpwA1hzI7x4s0me7uJzwVU5YtJqqXcX39yQCEuHuNhlhvFK/E1gcBS8\n+N7KqyBDAKoSJwNldDu500o0TGpxZYELKATeEAUa3hBFlh/LGQekXSZkuOXk6BFi\nqSR67IG2KOI4VBB5MV/oeL3yCQKBgQDlN6TpA6fQfQjKTLnYrjfW8YKVXgwv2EZt\ncpdFcaOd8Xe8D4tZFQFmV2nFFpezONwil4xuA0HbD8nrgen8N+bcwoAEhNKV477a\nkbd25CeoUM1uGU2LD8Q7w0ooDLcZ55Vf/8Sxc32DmRShzMFUFNUemCio48WFoZ2k\nJ+VM1WAvnwKBgGp/eXqzdwQuAECYF1TRB77SibYfRDu8+cGcgACTDzQEMTURxryz\n39cr+AetVF5rf6S8c4IzCt8MkCHSPvj5/w6a+gK+M2yfHtgLjFBJWD7eZDz3awMW\nfKjqi49f7/Cou0yyqaaACNI73+WnXo2L/aCtqxNpWN3/qv9vDMgwf4UhAoGBAIxv\nqDkfhTzGrpELqz3nl8y4kZIkWgEiWBwMfkQM2PsXC44MVAsTRJVIb0RSkEU9TBph\nkaeBlWK67LK/GPXv5iFRhY+/NSqiq7dMWgScyvNj9klDdXADC+61uwSIrdJQQgPc\nN82k/byYGLz9L2HtlZm2DgtT6hvyphwCWYnWnaTvAoGBAOyMPweiqUNteK3Mdjga\n7HE11oOzMEAW1V7EcV/KpWSRJlAUWx7XcNOjcu/5PwtbgnAPS/ku+BZ5yt3AyHAS\nD3tywITvTEngwkq5VbZLhq0GoN+bORs6nzoCB9AH5zg3ssrmiS71463Ehrl8Ecqa\nZkCqZkzZ2pE3Dqx9sV1VIXPW\n-----END PRIVATE KEY-----\n",
  "client_email": "myprojectrr@probable-axon-402219.iam.gserviceaccount.com",
  "client_id": "105148187935145358574",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/myprojectrr%40probable-axon-402219.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

#loadnewdata.py

def preguntar():
    while True:
        respuesta = input("¿Cumple con el requisito? (1: Sí, 2: No): ")
        if respuesta == "1":
            print("Requisito cumplido.")
            break
        elif respuesta == "2":
            print("Requisito no cumplido. Finalizando...")
            # Realiza cualquier acción de limpieza o manejo de errores aquí
            break
        else:
            print("Respuesta no válida. Por favor, elija 1 o 2.")

if __name__ == "__main__":
    preguntar()

#main.py #fastapi-websocket
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
SERVER_NAME = "Data-Scientist IA"
# Configurar el origen permitido en CORS (solo necesario si estás trabajando en desarrollo local)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ajusta esto según tus necesidades de seguridad
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

connected_clients = set()

@app.websocket("/chat/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await websocket.accept()
    connected_clients.add(websocket)

    try:
        # Inicio de la conversación desde el servidor
        await websocket.send_text(f"{SERVER_NAME}: Welcome, ¿Ready to start? 'Yes (1)' or 'no (2)'.")

        while True:
            user_response = await websocket.receive_text()
            if user_response == '1':
                await websocket.send_text(f"{SERVER_NAME}: Has iniciado la conversación.")
            elif user_response == '2':
                await websocket.send_text(f"{SERVER_NAME}: No has iniciado la conversación.")
            else:
                await websocket.send_text(f"{SERVER_NAME}: Respuesta no válida. Por favor, responde con 'si (1)' o 'no (2)'.")
    except WebSocketDisconnect:
        connected_clients.remove(websocket)

@app.get("/", response_class=HTMLResponse)
async def read_item():
    with open("static/index.html") as f:

        return HTMLResponse(content=f.read())

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


# validador.py

class Contador:
    def __init__(self):
        self.count = 0

    def validar_mensaje(self, mensaje):
        if mensaje.lower() == "hola":
            self.count += 1
            return f"Respuesta {self.count}"
        return None

contador = Contador()

#chat.html
<!DOCTYPE html>
<html>
<head>
    <title>Chat</title>
</head>
<body>
    <div>
        <h1>Chat</h1>
    </div>
    <div id="messages">
        <!-- Messages will be displayed here -->
    </div>
    <input type="text" id="messageInput" placeholder="Type your message...">
    <button id="sendButton">Send</button>

    <script>
        // JavaScript code for the chat interface
    </script>
</body>
</html>


#index.html
<!DOCTYPE html>
<html>
<head>
    <title>R-Ingenieria</title>
</head>
<body>
    <h1>Welcome To The Future</h1>
    <h4>_The Powerfull Program for Optimizing Industrial Process</h2>
        
    <div id="chat"></div>
    <input type="text" id="message" onkeydown="sendMessage(event)">
    <script>
        var chatDiv = document.getElementById('chat');
        var messageInput = document.getElementById('message');
        var socket = new WebSocket("ws://" + window.location.host + "/chat/1");

        socket.onmessage = function(event) {
            var p = document.createElement('p');
            p.innerHTML = event.data;
            chatDiv.appendChild(p);
        };

        function sendMessage(event) {
            if (event.key === "Enter") {
                socket.send(messageInput.value);
                messageInput.value = '';
            }
        }
    </script>
</body>
</html>
