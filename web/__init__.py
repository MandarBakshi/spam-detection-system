from flask import Flask, Blueprint

def CreateFlaskApp():
    flaskApp = Flask(__name__)
    from .views import views
    flaskApp.register_blueprint(views)

    return flaskApp