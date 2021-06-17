from flask import Flask

from app.auth import authentication


app = Flask(__name__)

app.register_blueprint(authentication, url_prefix="/auth")