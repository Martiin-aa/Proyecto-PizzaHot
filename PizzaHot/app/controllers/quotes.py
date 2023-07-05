"""Quote controllers."""

# Flask
from flask import render_template, redirect, request, url_for, session

# Config app
from app import app

# Models
from app.models.quote import Quote
from app.models.favorite import Favorite


@app.route("/quotes/")
def dashboard():
    """
    Página dashboard.

    La función `dashboard()` es una función de vista, lo que significa que se
    ejecuta cuando el usuario visita la ruta /quotes/ en el navegador.
    Ejemplo: http://localhost:5000/quotes/

    Parámetros:
        Ninguno
    Contexto:
        quotes (list): Lista de citas sin favoritos
        favorite_quotes (list): Lista de citas favoritas
    Retorna:
        render_template: Renderiza la plantilla quotes/dashboard.html
    """

    # Proteger la ruta /dashboard/
    if "user" not in session:
        return redirect(url_for("index"))

    # Obtener el ID del usuario de la sesión.
    data = {"user_id": session['user']['id']}

    quotes = Quote.get_all(data)
    favorite_quotes = Favorite.get_favorites(data)

    context = {
        "quotes": quotes,
        "favorite_quotes": favorite_quotes
    }
    return render_template("quotes/dashboard.html", **context)


@app.route("/quotes/<int:quote_id>/favorite/")
def add_favorite_quote(quote_id):
    """
    Agregar una cita a favoritos.

    La función `add_favorite_quote()` es una función de vista, lo que significa que se
    ejecuta cuando el usuario da clic en el botón agregar una cita a favoritos.
    Ejemplo: http://localhost:5000/quotes/1/favorite/

    Parámetros:
        quote_id (int): ID de la cita
    Retorna:
        redirect: Redirecciona a la función `dashboard()`
    """

    # Proteger la ruta /quotes/<int:quote_id>/favorite/
    if "user" not in session:
        return redirect(url_for("index"))

    data = {
        "quote_id": quote_id,
        "user_id": session['user']['id']
    }
    Favorite.add_favorite(data)
    return redirect(url_for("dashboard"))


@app.route("/quotes/<int:quote_id>/remove/")
def remove_favorite_quote(quote_id):
    """
    Eliminar una cita de favoritos.

    La función `remove_favorite_quote()` es una función de vista, lo que significa que se
    ejecuta cuando el usuario da clic en el botón remover una cita de favoritos.
    Ejemplo: http://localhost:5000/quotes/1/remove/

    Parámetros:
        quote_id (int): ID de la cita
    Retorna:
        redirect: Redirecciona a la función `dashboard()`
    """

    # Proteger la ruta /quotes/<int:quote_id>/remove/
    if "user" not in session:
        return redirect(url_for("index"))

    data = {
        "quote_id": quote_id,
        "user_id": session['user']['id']
    }
    Favorite.delete(data)
    return redirect(url_for("dashboard"))


@app.route("/quotes/<int:quote_id>/delete/")
def delete_quote(quote_id):
    """
    Eliminar una cita.

    La función `delete_quote()` es una función de vista, lo que significa que se
    ejecuta cuando el usuario da clic en el botón eliminar una cita.
    Ejemplo: http://localhost:5000/quotes/1/delete/

    Parámetros:
        quote_id (int): ID de la cita
    Retorna:
        redirect: Redirecciona a la función `dashboard()`
    """

    # Proteger la ruta /quotes/<int:quote_id>/delete/
    if "user" not in session:
        return redirect(url_for("index"))

    data = {"quote_id": quote_id}
    Quote.delete(data)
    return redirect(url_for("dashboard"))


@app.route("/quotes/create/", methods=["POST"])
def create_quote():
    """
    Crear una cita.

    La función `create_quote()` es una función de vista, lo que significa que se
    ejecuta cuando el usuario da clic en el botón crear una cita.
    Ejemplo: http://localhost:5000/quotes/create/

    Parámetros:
        Ninguno
    Retorna:
        redirect: Redirecciona a la función `dashboard()`
    """

    # Proteger la ruta /quotes/create/
    if "user" not in session:
        return redirect(url_for("index"))

    # Diccionario
    data = {
        "author": request.form['author'],
        "message": request.form['message'],
        "user_id": session['user']['id']
    }
    Quote.create(data)
    return redirect(url_for("dashboard"))


@app.route("/quotes/<int:quote_id>/", methods=["GET", "POST"])
def update_quote(quote_id):
    """
    Actualizar una cita.

    La función `update_quote()` es una función de vista, lo que significa que se
    ejecuta cuando el usuario da clic en el botón actualizar una cita.
    Ejemplo: http://localhost:5000/quotes/1/

    Parámetros:
        quote_id (int): ID de la cita
    Retorna:
        redirect: Redirecciona a la función `dashboard()`
    """

    # Proteger la ruta /quotes/<int:quote_id>/
    if "user" not in session:
        return redirect(url_for("index"))

    # Diccionario
    data = {"quote_id": quote_id}
    quote = Quote.get_one(data)

    if request.method == "POST":
        data = {
            "quote_id": quote_id,
            "author": request.form['author'],
            "message": request.form['message']
        }
        Quote.update(data)
        return redirect(url_for("dashboard"))
    return render_template("quotes/quote_update.html", quote=quote)
