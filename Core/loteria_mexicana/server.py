## R. Alvarez, Python Bootcamp, Jan 2025
## Exercicio <core> "Loteria mexicana"

from flask import Flask, render_template 
import random

app = Flask(__name__)

cores = ['#dda8c4', '#287fe4', '#eadb00', '#42ea00', '#ea2f00', '#8100ea', '#a4ea00', '#ffffff', '#964b00', '#ff7400', '#000000']

cartas = ["1  El Gallo", "2  El Diablito", "3  La Dama", "4  El catrín", "5  El paraguas", "6  La sirena", "7  La escalera", "8  La botella", "9  El barril", "10 El árbol", "11 El melón", "12 El valiente", "13 El gorrito", "14 La muerte", "15 La pera", "16 La bandera", "17 El bandolón", "18 El violoncello", "19 La garza", "20 El pájaro", "21 La mano", "22 La bota", "23 La luna", "24 El cotorro", "25 El borracho", "26 El negrito", "27 El corazón", "28 La sandía", "29 El tambor", "30 El camarón", "31 Las jaras", "32 El músico", "33 La araña", "34 El soldado", "35 La estrella", "36 El cazo", "37 El mundo", "38 El apache", "39 El nopal", "40 El alacrán", "41 La rosa", "42 La calavera", "43 La campana", "44 El cantarito", "45 El venado", "46 El sol", "47 La corona", "48 La chalupa", "49 El pino", "50 El pescado", "51 La palma", "52 La maceta", "53 El arpa", "54 La rana"]

@app.route('/<int:x>/<int:y>/', defaults={'z': 3})
@app.route('/<int:x>/<int:y>/<int:z>')
def loteria(x, y, z):
    numero_cartas = x * y
    if (numero_cartas > len(cartas)):
        repeticoes = numero_cartas // len (cartas)
        resto = numero_cartas % len (cartas)
        cartas_final = cartas * repeticoes + random.sample (cartas, resto) 
        cartas_mostrar = random.sample (cartas_final, (repeticoes * len(cartas) + resto))
    else:
        cartas_mostrar = random.sample (cartas, numero_cartas)
    if (z<=len(cores)):
        cores_validas = z
    else:
        cores_validas = len(cores)
    if (z == 3):
        txt_cores = "Cores: default"
    else:
        txt_cores = "Cores: " + str (z)
    if y <= 14:
        proporcao = 1
    else:
        proporcao = 14 / y
    return render_template('index.html', cores=cores, linhas = x, colunas = y, display=cartas_mostrar, quantas_cores=cores_validas, explica_cores=txt_cores, proporcao=proporcao)

@app.route('/loteria')
def loteria_default ():
    numero_cartas = 16
    cartas_mostrar = random.sample (cartas, numero_cartas)
    txt_cores = "Cores: default"
    cores_validas = 3
    proporcao = 1
    return render_template('index.html', cores=cores, linhas = 4, colunas = 4, display=cartas_mostrar, quantas_cores=cores_validas, explica_cores=txt_cores, proporcao=proporcao)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('vazio.html')

if __name__=="__main__":   

    app.run(debug=True)