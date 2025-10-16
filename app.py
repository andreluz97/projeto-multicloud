from flask import Flask, render_template

app = Flask(__name__)
contador = 0

@app.route('/')
def index():
    global contador
    contador += 1
    return render_template('index.html', contador=contador)

if __name__ == '__main__':
    app.run()
