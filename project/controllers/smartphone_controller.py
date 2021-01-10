from project import socketio
import requests

@socketio.on("confirmUser")
def user_confirm():
    url = "localhost:5001/get-confirmation"

    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers)
    print(response.text)
