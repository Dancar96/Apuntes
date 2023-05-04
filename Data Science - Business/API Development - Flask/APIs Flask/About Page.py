from flask import Flask

app = Flask(__name__) # Constructor que crea la aplicación Flask.

@app.route("/about") # Aplicación web básica con una sola ruta (/about) que devuelve "About Page" como respuesta
def about():
    return "About page"

app.run()