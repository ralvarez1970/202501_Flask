## R. Alvarez, Python Bootcamp, Jan 2025
## Exercicio <pratica> "Loteria Mexicana 2"

from flask import Flask, render_template, request, redirect, session

import random

cartas = ["0 - Carta inválida",

        "1  El Gallo",

        "2  El Diablito",

        "3  La Dama",

        "4  El catrín",

        "5  El paraguas",

        "6  La sirena",

        "7  La escalera",

        "8  La botella",

        "9  El barril",

        "10 El árbol",

        "11 El melón",

        "12 El valiente",

        "13 El gorrito",

        "14 La muerte",

        "15 La pera",

        "16 La bandera",

        "17 El bandolón",

        "18 El violoncello",

        "19 La garza",

        "20 El pájaro",

        "21 La mano",

        "22 La bota",

        "23 La luna",

        "24 El cotorro",

        "25 El borracho",

        "26 El negrito",

        "27 El corazón",

        "28 La sandía",

        "29 El tambor",

        "30 El camarón",

        "31 Las jaras",

        "32 El músico",

        "33 La araña",

        "34 El soldado",

        "35 La estrella",

        "36 El cazo",

        "37 El mundo",

        "38 El apache",

        "39 El nopal",

        "40 El alacrán",

        "41 La rosa",

        "42 La calavera",

        "43 La campana",

        "44 El cantarito",

        "45 El venado",

        "46 El sol",

        "47 La corona",

        "48 La chalupa",

        "49 El pino",

        "50 El pescado",

        "51 La palma",

        "52 La maceta",

        "53 El arpa",

        "54 La rana"]

def inicializar ():
    session['numero_carta'] = random.randint(1, 54)
    session['carta'] = cartas [session['numero_carta']]
    session['texto'] = "Tente adivinhar o número!"
    session['color'] = "yellow"
    session['tentativas'] = 0
    session['texto_contagem'] = ""
    return  

app = Flask(__name__)

app.secret_key = 'your_secret_key' 


@app.route('/')
def home():
    if 'numero_carta' not in session:
        inicializar()    
    return render_template('index.html', texto=session['texto'], color=session['color'], texto_contagem=session['texto_contagem'])

@app.route('/verifica_carta/', methods=['POST'])
def verifica ():
    session['tentativas'] += 1
    if int(request.form.get('escolha_usuario')) == session['numero_carta']:
        return redirect ('/acerto/')
    elif int(request.form.get('escolha_usuario')) > session['numero_carta']:
        session['texto'] = "O número escolhido é maior que o número da carta!"
        session['color'] = "red"
    else:
        session['texto'] = "O número escolhido é menor que o número da carta!"
        session['color'] = "red"
    if session['tentativas'] == 5:
        return redirect ('/termino/')
    return redirect ('/')

@app.route('/acerto/')
def acerto ():
    session['texto'] = f"Parabéns! O número escolhido é {session['numero_carta']} e a sua carta é <{session['carta']}>!"
    session['color'] = "green"
    session['texto_contagem'] = f"Você tentou {session['tentativas']} vezes até acertar."
    return render_template('acerto_termino.html', texto=session['texto'], color=session['color'], texto_contagem=session['texto_contagem'])

@app.route('/termino/')
def termino ():
    session['texto'] = "Você atingiu o limite de tentativas."
    session['color'] = "red"
    session['texto_contagem'] = ""
    return render_template('acerto_termino.html', texto=session['texto'], color=session['color'], texto_contagem=session['texto_contagem'])

@app.route('/jogar_novamente/')
def clear_session():
    session.clear()
    return redirect ('/')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('vazio.html')

if __name__=="__main__":   
    app.run(debug=True)