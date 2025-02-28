from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    num_fresa = int(request.form['fresa'])
    num_frambuesa = int(request.form['frambuesa'])
    num_manzana = int(request.form['manzana'])
    quantidade = num_fresa + num_frambuesa + num_manzana
    return render_template("checkout.html", quantidade=quantidade)


@app.route('/fruits')         
def fruits():
    return render_template("frutas.html")

if __name__=="__main__":   
    app.run(debug=True)    