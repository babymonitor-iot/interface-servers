import eventlet

eventlet.monkey_patch()
from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS
from flask_babel import Babel


app = Flask(__name__)
CORS(app)
babel = Babel(app)
socketio = SocketIO(app, async_mode="eventlet", cors_allowed_origins='*')


from .controllers import (
    main_controller,
    babymonitor_controller,
    smartphone_controller,
    smarttv_controller,
)
