from flask import Flask
from flask_twitter.TwitterPlugin import *
app = Flask(__name__)

@app.route('/')
@twitter_login
def hello_world(api=None):
    return "Hello"

@app.route("/twitter/callback")
@twitter_callback
def callback():
    return make_response("test");

if __name__ == '__main__':
    app.debug = True;
    app.run()
