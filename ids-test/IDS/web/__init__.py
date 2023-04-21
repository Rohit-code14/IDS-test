from flask import Flask
from .auth import auth
from .dbUtils import dbInit
# from .feature import feature

con = 0
def createApp():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = "abcdef"
    dbInit()

    app.register_blueprint(auth)
    # app.register_blueprint(feature)

    return app