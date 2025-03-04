## R. Alvarez, Python Bootcamp, Jan 2025
## Exercicio <pratica> "Juego del Destino"

from flask import Flask, render_template, request, redirect, session

import random


def inicializar ():
    session['nome'] = ""
    session['lugar'] = ""
    session['numero'] = ""
    session['comida'] = ""
    session['profissao'] = ""
    return  

app = Flask(__name__)

app.secret_key = 'your_secret_key' 

@app.route('/')
def home():
    if 'nome' not in session:
        inicializar()    
    return render_template('index.html')

@app.route('/enviar/', methods = ['POST'])
def enviar ():
    session['nome'] = request.form.get('nome')
    session['lugar'] = request.form.get('lugar')
    session['numero'] = request.form.get('numero')
    session['comida'] = request.form.get('comida')
    session['profissao'] = request.form.get('profissao')
    return redirect ('/futuro/')

@app.route('/futuro/')
def futuro ():
    session['sorte'] = random.randint(1, 10)
    return render_template ('futuro.html', nome=session['nome'], lugar=session['lugar'], numero=session['numero'], comida=session['comida'], profissao=session['profissao'], sorte=int(session['sorte']))

@app.route('/jogar_novamente/')
def clear_session():
    session.clear()
    return redirect ('/')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('vazio.html')

if __name__=="__main__":   
    app.run(debug=True)