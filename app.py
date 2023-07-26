#importar flask y render template
from flask import Flask, render_template

#crear una variable con la clase flask
app=Flask(__name__)

#creacion de rutas

#base de la header y el fouter
@app.route("/")
def ruta_principal():
    return render_template("base.html")

#ruta de la home page
@app.route("/homepage")
def homepage():
    return render_template("homepage.html")

#ruta de la landing page
@app.route('/landingpage')
def landing():
    return render_template("landingpage.html")






 
# va al fondo porque sirve para darle funcionalidad al boton de play o compilador de arriba 
if __name__ == '__main__': 
    app.run (debug=True)