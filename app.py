from flask import Flask


app = Flask(__name__)

@app.route('/')


def hello_world():
    return '¡Hola, mundo! Esta es mi primera aplicación web en Flask.'

def index():
    return render_template('index.html')

#item1 = Item["Tacos"]


if __name__ == '__main__':
    app.run(port=8080)

