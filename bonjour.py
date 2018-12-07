from flask import Flask
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})


app = Flask(__name__)



@app.route("/fr")
def bonjour():
    return "Bonjour, Monde!"


@app.route("/")
def hello():
    reply = bonjour()
    app.logger.info(reply)
    return reply 

@app.route("/es")
def buenasdias():
    reply = "buenas dias, mundo"
    app.logger.info(reply)
    return reply

@app.route("/en")
def goodday():
    return hello() 

@app.route("/he")
def shalom():
    return "Shalom, Olam"




