from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "Aplicação Flask no Azure funcionando!"

if __name__ == '__main__':
    app.run()
