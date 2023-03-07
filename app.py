# Building Url Dynamically
# Variable Rules and URL Building
from flask import Flask
# WSGI application
app = Flask(__name__)


@app.route('/')
def welcome():
    return "Welcome to my YouTube Channel"


@app.route('/dilli')
def dilliram():
    return "Welcome dear valued subscribers!"


@app.route('/success/<int:score>')
def success(score):
    return "Person is passed with the score" + str(score)


@app.route('/failure/<int:score>')
def failure(score):
    return "Person is failed with the score" + str(score)

# Result checker


@app.route('/result/<int:score>')
def result(score):
    result = ""
    if score < 50:
        result = "fail"
    else:
        score = "pass"
    return result


if __name__ == "__main__":
    app.run(debug=True)
