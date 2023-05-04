from flask import Flask

app = Flask(__name__) # Constructor que crea la aplicación Flask.

@app.route("/") # Aplicación web básica con una sola ruta (/) que devuelve "Hello, World!" como respuesta.
def hello():
    return "Hello, World!"

app.run()