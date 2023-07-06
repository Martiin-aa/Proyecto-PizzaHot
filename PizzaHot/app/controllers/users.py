"""User controllers."""

# Flask
from flask import render_template, request, redirect, url_for, flash, session
from flask_bcrypt import Bcrypt  

# Config app
from app import app

# Models
from app.models.user import User
from app.models.pizza import Pizza


# Bcrypt app
bcrypt = Bcrypt(app)


@app.route("/")
def index_register():
    """
    Index page.

    La función `index()` es una función de vista, lo que significa que se
    ejecuta cuando el usuario visita la ruta / en el navegador.
    Ejemplo: http://localhost:5000/

    Parámetros:
        Ninguno
    Retorna:
        render_template: Renderiza la plantilla users/auth/index_register.html
    """

    return render_template("users/auth/index_register.html")

@app.route("/login/")
def index_login():
    """
    Index page.

    La función `index()` es una función de vista, lo que significa que se
    ejecuta cuando el usuario visita la ruta / en el navegador.
    Ejemplo: http://localhost:5000/

    Parámetros:
        Ninguno
    Retorna:
        render_template: Renderiza la plantilla users/auth/index_login.html
    """

    return render_template("users/auth/index_login.html")


@app.route("/success/")
def success():
    """
    Success page.

    La función `success()` es una función de vista, lo que significa que se
    ejecuta cuando el usuario inicia sesión.
    Ejemplo: http://localhost:5000/success/

    Parámetros:
        Ninguno
    Retorna:
        render_template: Renderiza la plantilla dashboard.html
    """

    # Proteger la ruta /success/
    if "user" not in session:
        return redirect(url_for("index_register"))

    return render_template("dashboard.html")


@app.route("/login/", methods=["POST"])
def login():
    """
    Iniciar sesión.

    La función `login()` es una función de vista, lo que significa que se
    ejecuta cuando el usuario da clic en el botón iniciar sesión.
    Ejemplo: http://localhost:5000/login/

    Parámetros:
        Ninguno
    Retorna:
        redirect: Redirecciona a la ruta /success/ si el usuario inicia sesión
    """

    data = {
        "email": request.form["email"],
        "password": request.form["password"]
    }
    user = User.get_by_email(data)

    if user:
        is_correct_password = bcrypt.check_password_hash(user.password, data["password"])
        if is_correct_password:
            user = {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "adress": user.adress,
                "city": user.city
            }
            session["user"] = user
            flash("¡Bienvenido de nuevo!", "success")
            return redirect(url_for("success"))
        
    flash("¡Email o contraseña incorrectos!", "danger")
    return redirect(url_for("index_login"))


@app.route("/logout/")
def logout():
    """
    Cerrar sesión.

    La función `logout()` es una función de vista, lo que significa que se
    ejecuta cuando el usuario visita la ruta /logout/ en el navegador.
    Ejemplo: http://localhost:5000/logout/

    Parámetros:
        Ninguno
    Retorna:
        redirect: Redirecciona a la función `index()`
    """

    # Proteger la ruta /logout/
    if "user" not in session:
        return redirect(url_for("index_register"))

    session.clear()
    flash("¡Hasta luego!", "success")
    return redirect(url_for("index_register"))


@app.route("/register/", methods=["POST"])
def register(): 
    """
    Registrar usuario.

    La función `register()` es una función de vista, lo que significa que se
    ejecuta cuando el usuario da clic en el botón registrar.
    Ejemplo: http://localhost:5000/register/

    Parámetros:
        Ninguno
    Retorna:
        redirect: Redirecciona a la ruta /success/ si el usuario se registra
    """

    # Validacion del correo electronico
    if not User.validate_register(request.form):
        return redirect(url_for("index_register"))

    # Encriptar contraseña
    password_hash = bcrypt.generate_password_hash(request.form["password"])

    # Diccionario de datos para el modelo
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "adress": request.form["adress"],
        "city": request.form["city"],
        "password": password_hash
    }

    # Validar que el correo electrónico no esté registrado
    if User.get_by_email(data):
        flash("¡El correo electrónico ya está registrado!", "danger")
        return redirect(url_for("index_register"))
    
    # Registrar usuario
    id = User.register(data)
    session["user"] = id
    flash("¡Registro exitoso!", "success")
    return redirect(url_for("success"))


@app.route("/users/<int:user_id>/") #data
def user_detail(user_id):
    """
    Detalle de usuario.

    La función `user_detail()` es una función de vista, lo que significa que se
    ejecuta cuando el usuario visita la ruta /users/<int:user_id>/ en el navegador.
    Ejemplo: http://localhost:5000/users/1/

    Parámetros:
        user_id (int): El ID del usuario
    Contexto:
        user (object): Objeto del usuario
        number_pizzas (int): Número de pizzas del usuario
    Retorna:
        render_template: Renderiza la plantilla users/user_detail.html
    """

    # Proteger la ruta /users/<int:user_id>/
    if "user" not in session:
        return redirect(url_for("index_register"))

    data = {"user_id": user_id}
    user = User.get_one(data)
    number_pizzas = Pizza.get_number_of_pizzas(data)

    context = {
        "user": user,
        "number_pizzas": number_pizzas
    }
    return render_template("users/user_detail.html", **context)


