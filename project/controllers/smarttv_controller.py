from project import socketio
import requests

@socketio.on("changeStatus")
def change_status(lock):
    url = "localhost:5002/change_status"

    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data={'lock': lock})
    print(response.text)

