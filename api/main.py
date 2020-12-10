from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    request_method = request.method
    if request_method == 'POST':
        print('---------------')
        print(request.form)
        print('---------------')
        return redirect(url_for('name'))
    return render_template('helloform.html', request_method = request_method)

@app.route('/name')
def name():
    return 'name'

if __name__ == "__main__":
    app.run(debug = True)