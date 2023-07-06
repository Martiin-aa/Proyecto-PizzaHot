"""Pizza controllers."""

# Flask
from flask import render_template, redirect, request, url_for, session

# Config app
from app import app

# Models
from app.models.pizza import Pizza
from app.models.order import Order


@app.route("/orders/")
def dashboard():
    """
    Página dashboard.
    """

    # Proteger la ruta /dashboard/
    if "user" not in session:
        return redirect(url_for("index_register"))

    print(session['user'])

    # Obtener el ID del usuario de la sesión.
    data = {"user_id": session['user']}

    order_past_pizzas = Order.get_past_orders(data)
    order_pizzas = Order.get_orders(data)

    context = {
        "order_past_pizzas": order_past_pizzas,
        "order_pizzas": order_pizzas
    }
    return render_template("dashboard.html", **context)

@app.route("/pizzas/")
def pizzas():
    """
    Página dashboard.
    """

    # Proteger la ruta /dashboard/
    if "user" not in session:
        return redirect(url_for("index_register"))

    print(session['user'])

    # Obtener el ID del usuario de la sesión.
    data = {"user_id": session['user']}

    pizzas = Pizza.get_all(data)

    context = {
        "pizzas": pizzas
    }
    return render_template("pizzas/pizzas.html", **context)


@app.route("/pizzas/<int:pizza_id>/delete/")
def delete_pizza(pizza_id):
    """
    Eliminar una pizza.
    """

    # Proteger la ruta /pizzas/<int:pizza_id>/delete/
    if "user" not in session:
        return redirect(url_for("index_register"))

    data = {"pizza_id": pizza_id}
    Pizza.delete(data)
    return redirect(url_for("dashboard"))


@app.route("/pizzas/create/", methods=["POST"]) #data
def create_pizza():
    """
    Crear una pizza.
    """

    # Proteger la ruta /pizzas/create/
    if "user" not in session:
        return redirect(url_for("index_register"))

    # Diccionario
    data = {
        "name": request.form['name'],
        "size": request.form['size'],
        "crust": request.form['crust'],
        "user_id": session['user']['id']
    }
    Pizza.create(data)
    return redirect(url_for("dashboard"))


@app.route("/pizzas/<int:pizza_id>/", methods=["GET", "POST"]) #data
def update_pizza(pizza_id):
    """
    Actualizar una pizza.
    """

    # Proteger la ruta /pizzas/<int:pizza_id>/
    if "user" not in session:
        return redirect(url_for("index_register"))

    # Diccionario
    data = {"pizza_id": pizza_id}
    pizza = Pizza.get_one(data)

    if request.method == "POST":
        data = {
            "pizza_id": pizza_id,
            "name": request.form['name'],
            "size": request.form['size'],
            "crust": request.form['crust'],
            "price": request.form['price'],
        }
        Pizza.update(data)
        return redirect(url_for("dashboard"))
    return render_template("pizzas/pizza_update.html", pizza=pizza)
