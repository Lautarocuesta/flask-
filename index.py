from flask import Flask, render_template

app = Flask(__name__)


"""
@app.route("/")
def principal():
    return "bienvenue" """

@app.route("/")
def principal():
    return render_template ("index.html")

@app.route("/contacto")
def contacto():
    return "contactos"

if __name__== '__main__':
    app.run(debug=True, port=5000)

