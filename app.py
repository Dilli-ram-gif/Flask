from flask import Flask
# WSGI application
app = Flask(__name__)


@app.route('/')
def welcome():
    return "Welcome to my YouTube Channel"


@app.route('/dilli')
def dilliram():
    return "Welcome dear valued subscribers!"


if __name__ == "__main__":
    app.run(debug=True)
