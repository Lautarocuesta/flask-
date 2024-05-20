from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def principal():
    return render_template("index.html")

@app.route("/contacto")
def contacto():
    nombres = ["Juan", "María", "Carlos", "Laura", "Pedro", "Ana", "Luis", "Sofía"]
    return render_template("contacto.html", nombres=nombres)

@app.route("/bienvenida")
def bienvenida():
    usuario = "Carlos"
    articulos = [
        {"nombre": "Laptop", "precio": 1200},
        {"nombre": "Mouse", "precio": 25},
        {"nombre": "Teclado", "precio": 45}
    ]
    return render_template("bienvenida.html", usuario=usuario, articulos=articulos)
@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    nombre = request.form['nombre']
    email = request.form['email']
    mensaje = request.form['mensaje']
    # Aquí puedes procesar los datos del formulario (por ejemplo, guardarlos en una base de datos o enviar un correo electrónico)
    return redirect(url_for('contacto'))


if __name__ == '__main__':
    app.run(debug=True, port=5000)
