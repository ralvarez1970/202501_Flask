## R. Alvarez, Python Bootcamp, Jan 2025
## Exercicio <core> "Loteria mexicana"

from flask import Flask, render_template 

app = Flask(__name__)

paises = [

        {'pais': 'Argentina' , 'capital': 'Buenos Aires'},

        {'pais': 'Brasil' , 'capital': 'Brasilia'},

        {'pais': 'Chile' , 'capital': 'Santiago de Chile'},

        {'pais': 'Colombia' , 'capital': 'Bogotá'},

        {'pais': 'Costa Rica' , 'capital': 'San José'},

        {'pais': 'Paraguay' , 'capital': 'Asunción'},

        {'pais': 'Perú' , 'capital': 'Lima'}

]

@app.route('/paises')
def gera_tabela():
    return render_template('index.html', paises=paises)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('vazio.html')

if __name__=="__main__":   

    app.run(debug=True)