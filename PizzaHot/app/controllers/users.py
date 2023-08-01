"""User controllers."""

import os

# Flask
from flask import render_template, request, redirect, url_for, flash, session
from flask_bcrypt import Bcrypt
from flask_mail import Mail, Message
from werkzeug.utils import secure_filename

# Config app
from app import app

app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = 'e51bdda7a1c9c4'
app.config['MAIL_PASSWORD'] = '0b40666a5edd9f'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

# Models
from app.models.user import User
from app.models.address import Address
from app.models.order import Order

# Bcrypt app
bcrypt = Bcrypt(app)


@app.route("/")
def index_register():
    """
    Index, Pagina de registro.
    """

    return render_template("users/auth/index_register.html")

@app.route("/login/")
def index_login():
    """
    Index, Pagina de inicio session.
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
                "email": user.email
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

    if not User.validate_register(request.form):
        return redirect(url_for("index_register"))

    password_hash = bcrypt.generate_password_hash(request.form["password"])

    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": password_hash
    }

    if User.get_by_email(data):
        flash("¡El correo electrónico ya está registrado!", "danger")
        return redirect(url_for("index_register"))
    
    user = User.register(data)
    if user:
        session["user"] = {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email
        }
        flash("¡Registro exitoso!", "success")
        return redirect(url_for("dashboard"))

    return redirect(url_for("index_register"))

@app.route("/users/update/", methods=["GET", "POST"])
def update_user():
    """
    Actualizar un usuario.
    """

    if "user" not in session:
        return redirect(url_for("index_register"))

    user = User.get_one({"id": session["user"]["id"]})
    address = Address.get_one({"user_id": session["user"]["id"]})
    data = {"id": session["user"]["id"]}
    
    if request.method == "POST":
        user_data = {
            "user_id": session["user"]["id"],
            "first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
            "email": request.form["email"]
        }
        
        User.update(user_data)
        flash("!Usuario actualizado exitosamente!", "success")
        return redirect(url_for("dashboard"))

    context = {
        "user": user,
        "address": address,
        "count_pizzas": show_count_pizzas(data)
    }

    return render_template("users/user_update.html", **context)

@app.route("/users/update/address/", methods=["POST"])
def update_address():
    """
    Actualizar la dirección de un usuario.
    """

    if "user" not in session:
        return redirect(url_for("index_register"))

    if request.method == "POST":

        address_data = {
            "user_id": session["user"]["id"],
            "district": request.form["district"],
            "address": request.form["address"],
            "house_number": request.form["house_number"],
            "telephone": request.form["telephone"]
        }

        Address.update(address_data)
        flash("¡Dirección actualizada exitosamente!", "success")
        return redirect(url_for("dashboard"))

@app.route("/users/update/logo/", methods=["POST"])
def update_user_logo():
    """
    Actualizar la foto de perfil.
    """

    if "user" not in session:
        return redirect(url_for("index_register"))

    if request.method == "POST":        
        if "file" not in request.files:
            flash("No file part")
            return redirect(url_for("dashboard"))

        file = request.files["file"]

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)  

            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

            data = {
                "user_id": session["user"]["id"],
                "logo": filename,
            }

            User.update_photo(data)
            session["user"]["logo"] = filename
            flash("¡Foto de usuario actualizada exitosamente!", "success")
            return redirect(url_for("dashboard"))

@app.route("/display/<filename>/")
def display_image(filename):
    """
    Permite mostrar la imagen subida.
    """

    return redirect(url_for("static", filename="uploads/" + filename), code=301)


def allowed_file(filename) -> bool:
    """
    Comprueba si la extensión del archivo es válida.
    """

    return "." in filename and \
        filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]


@app.route("/information/contact/", methods=["GET", "POST"])
def information():
    """
    pagina de información y contacto.
    """

    if "user" not in session:
        return redirect(url_for("index_register"))
    
    data = {"id": session["user"]["id"]}

    if request.method == "POST":
        nombre = request.form["nombre"]
        email = request.form["email"]
        mensaje = request.form["mensaje"]

        msg = Message("Mensaje de contacto, Cliente PizzaHot",
                    sender=email,
                    recipients=["martin.arayaantezana@gmail.com"])
        
        msg.body = f"Nombre: {nombre}\nMensaje: {mensaje}"
        msg.html = f"<p><strong>Nombre del Cliente:</strong> {nombre}</p><p><strong>Mensaje:</strong> {mensaje}</p>"
        
        mail.send(msg)
        flash("!Correo enviado exitosamente!", "success")
        return redirect(url_for("dashboard"))
    
    context = {
        "count_pizzas": show_count_pizzas(data)
    }

    return render_template("information.html", **context)

def show_count_pizzas(data):
    """
    Muestra la cuenta de pizzas de la orden del usuario. deletable_1
    """
    
    count_pizzas = Order.get_count_pizzas(data)

    return count_pizzas

