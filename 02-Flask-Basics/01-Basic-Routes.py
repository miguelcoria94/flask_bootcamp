from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Welcome to my site</h1>"

@app.route('/about')
def info():
    return "<h1>This is the about page</h1>"


if __name__ == '__main__':
    app.run()
