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
    Index register page.
    """

    return render_template("users/auth/index_register.html")

@app.route("/login/")
def index_login():
    """
    Index login page.
    """

    return render_template("users/auth/index_login.html")

@app.route("/login/", methods=["POST"])
def login():
    """
    Iniciar sesión.
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
                "address": user.address,
                "city": user.city
            }
            session["user"] = user
            flash("¡Bienvenido de nuevo!", "success")
            return redirect(url_for("dashboard"))
        
    flash("¡Email o contraseña incorrectos!", "danger")
    return redirect(url_for("index_login"))


@app.route("/logout/")
def logout():
    """
    Cerrar sesión.
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
        "address": request.form["address"],
        "city": request.form["city"],
        "password": password_hash
    }

    # Validar que el correo electrónico no esté registrado
    if User.get_by_email(data):
        flash("¡El correo electrónico ya está registrado!", "danger")
        return redirect(url_for("index_register"))
    
    # Registrar usuario
    user = User.register(data)
    if user:
        session["user"] = {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "address": user.address,
            "city": user.city
        }
        flash("¡Registro exitoso!", "success")
        return redirect(url_for("dashboard"))

    return redirect(url_for("index_register"))