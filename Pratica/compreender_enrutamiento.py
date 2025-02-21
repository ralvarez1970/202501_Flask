
from flask import Flask  # Importa Flask para permitirnos crear nuestra aplicación

app = Flask(__name__)    

@app.route('/')          
def hola_mundo():
    return '<h1 style = "color : red">Olá! Welcome to Flasks world!</h1>'  

@app.route('/rota')          
def rota():
    return '<h1 style = "color : blue">Que rota vc está buscando?</h1>'  

@app.route('/welcome/<nome>')          
def greeting(nome):
    return f'<h1 style = "color : green">Bem-vind@ {str(nome)}</h1>'  

@app.route('/welcome/<quantidade>/<palavra>')          
def repetir(quantidade, palavra):
    vezes = int(quantidade)
    response = ""
    for i in range (1, vezes+1):
        response += f'<h1 style = "color : red">[{i}] Repita depois de mim: {palavra}</h1>'
    return response

@app.errorhandler(404)
def page_not_found(error):
    return '<h1 style="color: red">Sobrecarga de rotas. Não encontramos onde você quer ir. Tente novamente!</h1>', 404  # Returning 404 status code explicitly

if __name__=="__main__":  
    app.run(debug=True)    