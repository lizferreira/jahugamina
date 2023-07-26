from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def pagina_principal():
    return render_template("inicio.html")

@app.route('/landingpage')
def landing():
    return render_template("landingpage.html")



# va al fondo porque sirve para darle funcionalidad al boton de play o compilador de arriba 
if __name__ == '__main__': 
    app.run (debug=True)