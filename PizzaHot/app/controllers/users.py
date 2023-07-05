"""User controllers."""

# Flask
from flask import render_template, request, redirect, url_for, flash, session
from flask_bcrypt import Bcrypt  

# Config app
from app import app

# Models
from app.models.user import User
from app.models.quote import Quote


# Bcrypt app
bcrypt = Bcrypt(app)


@app.route("/")
def index():
    """
    Index page.

    La función `index()` es una función de vista, lo que significa que se
    ejecuta cuando el usuario visita la ruta / en el navegador.
    Ejemplo: http://localhost:5000/

    Parámetros:
        Ninguno
    Retorna:
        render_template: Renderiza la plantilla users/auth/index.html
    """

    return render_template("users/auth/index.html")


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
        render_template: Renderiza la plantilla users/auth/success.html
    """

    # Proteger la ruta /success/
    if "user" not in session:
        return redirect(url_for("index"))

    return render_template("users/auth/success.html")


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
                "name": user.name,
                "email": user.email
            }
            session["user"] = user
            flash("¡Bienvenido de nuevo!", "success")
            return redirect(url_for("success"))
        
    flash("¡Email o contraseña incorrectos!", "danger")
    return redirect(url_for("index"))


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
        return redirect(url_for("index"))

    session.clear()
    flash("¡Hasta luego!", "success")
    return redirect(url_for("index"))


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
        return redirect(url_for("index"))

    # Encriptar contraseña
    password_hash = bcrypt.generate_password_hash(request.form["password"])

    # Diccionario de datos para el modelo
    data = {
        "name": request.form["name"],
        "email": request.form["email"],
        "password": password_hash
    }

    # Validar que el correo electrónico no esté registrado
    if User.get_by_email(data):
        flash("¡El correo electrónico ya está registrado!", "danger")
        return redirect(url_for("index"))
    
    # Registrar usuario
    user = User.register(data)
    if user:
        session["user"] = {
            "id": user.id,
            "name": user.name,
            "email": user.email
        }
        flash("¡Registro exitoso!", "success")
        return redirect(url_for("success"))

    return redirect(url_for("index"))


@app.route("/users/<int:user_id>/")
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
        number_quotes (int): Número de citas del usuario
    Retorna:
        render_template: Renderiza la plantilla users/user_detail.html
    """

    # Proteger la ruta /users/<int:user_id>/
    if "user" not in session:
        return redirect(url_for("index"))

    data = {"user_id": user_id}
    user = User.get_one(data)
    number_quotes = Quote.get_number_of_quotes(data)

    context = {
        "user": user,
        "number_quotes": number_quotes
    }
    return render_template("users/user_detail.html", **context)


