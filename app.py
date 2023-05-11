from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello')
def hello_word():
    return 'Hello, world!'


@app.route('/hello/h1')
def hello_word_color():
    return '<h1 style="color:red">Hello, world!</h1>'


@app.route('/help')
def help():
    return 'help me'


@app.route('/contact')
def contact():
    return 'contact with me'


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        return f'{request.form["username"]} + {request.form["password"]}'
    else:
        return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True, host='localhost')
