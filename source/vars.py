from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hi():
    return render_template('hello.html', list_of_names = ['Chis', 'Rafa', 'Pizza'])

@app.route('/<string:name>')
def hello_world(name):
    return f'Hello, {name}!'

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug = True)