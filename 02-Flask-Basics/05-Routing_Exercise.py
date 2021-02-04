# Set up your imports here!
# import ...
from flask import Flask
app = Flask(__name__)


@app.route('/') # Fill this in!
def index():
    # Welcome Page
    # Create a generic welcome page.
    return '<h1>Welcome Page</h1>'

@app.route('/puppy/<name>') # Fill this in!
def puppylatin(name):
    # This function will take in the name passed
    # and then use "puppy-latin" to convert it!

    if name[len(name) - 1] != 'y':
        newname = name + "y"
    else:
        first_half = name[:-1]
        newname = first_half + "iful"
    # HINT: Use indexing and concatenation of strings
    # For Example: "hello"+" world" --> "hello world"
    return '<h1>your new name is {}<h1>'.format(newname)

if __name__ == '__main__':
    # Fill me in!
    app.run(debug=True)
