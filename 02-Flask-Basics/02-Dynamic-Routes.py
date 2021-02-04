from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Puppy!</h1>'

@app.route('/information')
def info():
    return '<h1>Puppies are cute!</h1>'

@app.route('/puppy/<id>')
def profile(id):
    return f'<h1>This is {id}\'s profile'


if __name__ == '__main__':
    app.run()
