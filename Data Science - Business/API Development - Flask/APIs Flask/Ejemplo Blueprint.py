from flask import Flask, Blueprint

# Creamos un objeto Blueprint llamado "auth_bp"
auth_bp = Blueprint('auth', __name__)

# Creamos una ruta "/login" dentro de "auth_bp"
@auth_bp.route('/login')
def login():
    return 'Página de inicio de sesión'

# Creamos una ruta "/register" dentro de "auth_bp"
@auth_bp.route('/register')
def register():
    return 'Página de registro'

# Creamos una instancia de Flask
app = Flask(__name__)

# Registramos el objeto Blueprint "auth_bp" con el prefijo de URL "/auth"
app.register_blueprint(auth_bp, url_prefix='/auth')

# Ejecutamos la aplicación Flask en el puerto 5000
if __name__ == '__main__':
    app.run()
