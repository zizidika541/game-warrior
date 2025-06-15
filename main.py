import flask
app = flask.Flask(__name__)

@app.route('/')
def index():
    return flask.send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def static_proxy(path):
    return flask.send_from_directory('.', path)
