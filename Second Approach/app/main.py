from flask import Flask

from controllers.auth import authentication
from controllers.user_post import user_post


app = Flask(__name__)

app.register_blueprint(authentication, url_prefix="/auth")
app.register_blueprint(user_post, url_prefix="/user_post")