from flask import Flask
from controller.library_controller import library_blueprint

app = Flask(__name__)

app.register_blueprint(library_blueprint)


