from flask import Flask, render_template, request, redirect, url_for # Importamos Flask, render_template, request, redirect y url_for.
from flask_sqlalchemy import SQLAlchemy # Importamos SQLAlchemy.
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required # Importamos varias clases de flask_login.

app = Flask(__name__) # Construimos la app.
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///usuarios.db" # Configuramos la URI (Uniform Resource Identifier) de la base de datos SQLite en la variable SQLALCHEMY_DATABASE_URI.
app.config["SECRET_KEY"] = "clave-secreta" # Configuramos una clave secreta para nuestra aplicación, necesaria para manejar sesiones de usuario.
db = SQLAlchemy(app) # Configuramos una clave secreta para nuestra aplicación, necesaria para manejar sesiones de usuario.
login_manager = LoginManager(app) # Creamos una instancia del manejador de autenticación de Flask-Login.

class Usuario(UserMixin, db.Model): # Define una clase Usuario que hereda de UserMixinpara tener métodos y atributos para manejar la autenticación con Flask-Login y de db.Model para definirse como tabla de la database.
    id = db.Column(db.Integer, primary_key=True) # Una columna 'id' como clave primaria.
    nombre_usuario = db.Column(db.String(50), unique=True, nullable=False) # Una columna 'nombre_usuario'.
    contrasena = db.Column(db.String(50), nullable=False) # Una columna 'contraseña'.

@login_manager.user_loader # Función que recibe un ID de usuario y devuelve el objeto Usuario correspondiente, necesario para que Flask-Login maneje la autenticación de usuarios.
def load_user(user_id):  # Función que recibe un ID de usuario y devuelve el objeto Usuario correspondiente, necesario para que Flask-Login maneje la autenticación de usuarios.
    return Usuario.query.get(int(user_id))

@app.route("/") # Creamos la ruta.
def index(): # Aqui se ejecutará la plantilla index.html.
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"]) # Creamos la ruta para la página de inicio de sesión que acepta solicitudes GET y POST.
def login(): # Función que manejará la solicitud para la ruta de inicio de sesión.
    if request.method == "POST": # Verificamos si la solicitud es de tipo POST (es decir, si se envió un formulario).
        nombre_usuario = request.form.get("nombre_usuario") # Obtenemos el valor del campo "nombre_usuario" del formulario enviado.
        contrasena = request.form.get("contrasena") # Obtenemos el valor del campo "contrasena" del formulario enviado.
        usuario = Usuario.query.filter_by(nombre_usuario=nombre_usuario).first() # Busca en la base de datos el usuario que tenga el mismo nombre de usuario ingresado en el formulario.
        if usuario is not None and usuario.contrasena == contrasena:
            login_user(usuario) # Si el usuario existe y la contraseña ingresada coincide con la que está almacenada en la base de datos, el usuario se inicia sesión utilizando la función login_user de Flask-Login.
            return redirect(url_for("index")) # Se redirige al usuario a la página de inicio después de iniciar sesión exitosamente utilizando la función redirect de Flask.
    return render_template("login.html") # Se accede a la página de inicio de sesión por primera vez o si la información ingresada no es correcta, se renderiza la plantilla login.html.

@app.route("/logout") # Creamos la ruta que será ejecutada cuando el usuario acceda a la ruta "/logout" de la aplicación.
@login_required # Verifica si el usuario está autenticado antes de ejecutar la función logout(). Si el usuario no está autenticado, se redirige a la página de inicio de sesión.
def logout(): 
    logout_user() # Función proporcionada por Flask-Login y se encarga de cerrar la sesión del usuario actual.
    return redirect(url_for("index")) # Después de cerrar la sesión del usuario, se redirige a la página de inicio de la aplicación.

if __name__ == "__main__":
    with app.app_context(): # Esto establecerá el contexto de la aplicación y nos permitirá llamar a db.create_all() correctamente.
        db.drop_all() # Elimina todas las tablas existentes.
        db.create_all() # Crea nuevas tablas utilizando los modelos definidos.
         # Crear un nuevo usuario
        nuevo_usuario = Usuario(nombre_usuario='Elba Surero', contrasena='Basurero') # Estas serán las credenciales.
        db.session.add(nuevo_usuario)
        db.session.commit()
    app.run(debug=True) # Inicia la aplicación en modo de depuración.