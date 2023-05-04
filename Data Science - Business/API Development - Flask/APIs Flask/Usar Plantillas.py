from flask import Flask, render_template # Importamos Flask y render_template.

app = Flask(__name__) # Construimos la app.

@app.route("/") # Creamos la ruta.
def index(): # Creamos una función que contextualice las variables que hemos creado en la plantilla de HTML.
    title = "Inicio"
    heading = "Bienvenido a mi aplicación web"
    content = "Esta es mi primera aplicación web con Flask"
    return render_template("index1.html", title=title, heading=heading, content=content)

app.run()