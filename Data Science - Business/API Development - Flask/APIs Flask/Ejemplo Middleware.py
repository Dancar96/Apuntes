from flask import Flask, request # # Importamos Flask y request.

app = Flask(__name__) # # Construimos la app.

@app.before_request # Decorador que registra la funcion before() para ser llamada antes de cada solicitud.
def before(): # Función que imprime "Antes de la solicitud" y los encabezados de la solicitud.
    print('Antes de la solicitud')
    print(request.headers)

@app.after_request # Decorador que registra la funcion after() para ser llamada después de cada solicitud.
def after(response): # Función que imprime "Después de la solicitud" y devuelve la respuesta que se le pasa como parámetro.
    print('Después de la solicitud')
    return response

@app.route('/') # Creamos la ruta que registra la función index() para manejar las solicitudes GET.
def index():
    return 'Hola, mundo!'

if __name__ == '__main__':
    app.run(debug=True) # Inicia la aplicación en modo de depuración.