"""Order controllers."""

# Flask
from flask import render_template, redirect, request, url_for, session

# Config app
from app import app

# Models
from app.models.pizza import Pizza
from app.models.order import Order

@app.route("/pizzas/<int:pizza_id>/order/")
def add_order_pizza(pizza_id):
    """
    Agregar una pizza a las ordenes.
    """

    # Proteger la ruta /pizzas/<int:pizza_id>/order/
    if "user" not in session:
        return redirect(url_for("index_register"))

    data = {
        "pizza_id": pizza_id,
        "user_id": session['user']['id']
    }
    Order.add_order(data)
    return redirect(url_for("dashboard"))


@app.route("/pizzas/<int:pizza_id>/remove/")
def remove_order_pizza(pizza_id):
    """
    Eliminar una pizza de la orden.
    """

    # Proteger la ruta /pizzas/<int:pizza_id>/remove/
    if "user" not in session:
        return redirect(url_for("index_register"))

    data = {
        "pizza_id": pizza_id,
        "user_id": session['user']['id']
    }
    Order.delete(data)
    return redirect(url_for("dashboard"))
