from project import socketio
from threading import Thread
import requests


bm_on = False

def generate_status():
    global bm_on
    url = "localhost:5000/bm_send"

    headers = {
    'Content-Type': 'application/json'
    }
    while bm_on:
        response = requests.request("GET", url, headers=headers)
        print(response.text)


@socketio.on('babymonitorConnect')
def babymonitor_connect():
    global bm_on
    bm_on = True

    Thread(target=generate_status).start()


@socketio.on("babymonitorDisconnect")
def babymonitor_disconnect():
    global bm_on
    bm_on = False
