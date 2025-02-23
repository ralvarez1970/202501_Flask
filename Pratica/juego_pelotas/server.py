

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/jogo/<quantidade>/<cor_pelota>')
def bienvenido(quantidade, cor_pelota):
    return render_template('index.html', vezes = int(quantidade), cor = cor_pelota)

if __name__=="__main__":   

    app.run(debug=True)