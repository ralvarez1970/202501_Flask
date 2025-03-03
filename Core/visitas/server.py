## R. Alvarez, Python Bootcamp, Jan 2025
## Exercicio <core> "Visitas"

from flask import Flask, render_template, request, redirect, session

sessoes = 1

app = Flask(__name__)

app.secret_key = 'your_secret_key' 

@app.route('/')
def home():
    global sessoes
    if 'visit' in session:
        session['visit'] += 1
    else:
        session['visit'] = 1
    contador=session['visit']
    if 'reset' not in session:
        session['reset'] = 0 
    if (contador == 1):
        plural = ""
    else:
        plural ="es"
    if (session['reset'] > 1):
        plural_reset = "es"
    else:
        plural_reset = ""
    return render_template('index.html', contador=contador, plural=plural, reset=session.get('reset'), plural_reset=plural_reset, sessoes=sessoes)

@app.route('/adjust/', methods=['POST'])
def adjust ():
    print(request.form)
    if (request.form.get('soma_dois') == 'yes'):
        session['visit'] += 2
    elif (request.form.get('zero') == 'yes'):
        session['visit'] = 1
        session['reset'] += 1
    if request.form.get('incremento', "").isdigit():
        session['visit'] += int(request.form.get('incremento')) - 1
    else:
        session['visit'] -= 1
    return redirect ('/')

@app.route('/destruir_sessao/')
def clear_session():
    global sessoes
    session.clear()
    sessoes += 1
    return redirect ('/')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('vazio.html')

if __name__=="__main__":   
    app.run(debug=True)