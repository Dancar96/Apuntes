from flask import Flask, render_template, request # Importamos Flask, render_template y request.
from flask_sqlalchemy import SQLAlchemy # Importamos SQLAlchemy

app = Flask(__name__) # Construimos la app.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///usuarios.db" # Configuramos la URI (Uniform Resource Identifier) de la base de datos SQLite en la variable SQLALCHEMY_DATABASE_URI.
db = SQLAlchemy(app)

class Usuario(db.Model): #define una clase Usuario que hereda de la clase db.Model de SQLAlchemy. Esta clase define la estructura de la tabla de la base de datos.
    id = db.Column(db.Integer, primary_key=True) # Una columna 'id' como clave primaria.
    nombre = db.Column(db.String(50), nullable=False) # Una columna 'nombre'.
    correo_electronico = db.Column(db.String(50), nullable=False) # Una columna 'correo_electronico'.

@app.route("/") # Creamos la ruta.
def index(): # Consultamos todos los registros de la tabla Usuario y los pasa a la plantilla HTML "usuarios.html" para que se muestren en la página web.
    usuarios = Usuario.query.all()
    return render_template("usuarios.html", usuarios=usuarios)

@app.route("/agregar", methods=["POST"]) # En esta ruta, mediante la petición 'POST' recuperamos los datos enviados por el formulario usuarios.html.
def agregar(): # Crea un nuevo objeto Usuario con esos datos y lo agrega a la base de datos mediante db.session.add() y db.session.commit().
    nombre = request.form.get("nombre")
    correo_electronico = request.form.get("correo_electronico")
    usuario = Usuario(nombre=nombre, correo_electronico=correo_electronico)
    db.session.add(usuario)
    db.session.commit()
    return "Usuario agregado"

if __name__ == "__main__":
    with app.app_context(): # Esto establecerá el contexto de la aplicación y nos permitirá llamar a db.create_all() correctamente.
        db.create_all()
        app.run(debug=True)

'''
Por último, especificamos que si se ejecuta este archivo de Python directamente, se creará la tabla Usuario en la base de datos utilizando db.create_all(). 
También se ejecutará la aplicación Flask utilizando app.run(), con el modo debug habilitado para que se muestren mensajes de depuración en la consola.

'''