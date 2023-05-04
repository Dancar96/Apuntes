from flask import Flask, render_template, request # Importamos Flask, render_template y request.

app = Flask(__name__) # Construimos la app.

@app.route("/") # Creamos la ruta.
def index(): # Aqui se ejecutará la plantilla del formulario.
    return render_template("form.html")

@app.route("/submit", methods=["POST"]) # En esta ruta, mediante la petición 'POST' procesaremos los datos que el usuario introdujo en el formulario.
def submit(): # Mediante request obtenemos los resultados.
    name = request.form.get("name")
    email = request.form.get("email")
    return f"Nombre: {name}, Correo electrónico: {email}"

app.run()