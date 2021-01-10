from project import app, socketio


if __name__ == "__main__":
    port = 5004
    print(f'Running BabyMonitorSoS with Dojot / port={port} \n')
    socketio.run(app, port=port)
