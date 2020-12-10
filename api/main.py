from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hi():
    return render_template('hello.html')

@app.route('/<string:name>')
def hello_world(name):
    return f'Hello, {name}!'


if __name__ == "__main__":
    app.run(debug = True)