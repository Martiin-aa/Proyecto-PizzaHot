"""Order controllers."""

# Flask
from flask import render_template, redirect, request, url_for, session

# Config app
from app import app

# Models
from app.models.order import User
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

@app.route("/orders/<int:user_id>/") 
def show_order(user_id):
    """
    Muestra la orden del usuario.
    """

    # Proteger la ruta /orders/<int:user_id>/
    if "user" not in session:
        return redirect(url_for("index_register"))

    data = {"user_id": user_id}
    user = User.get_one(data)
    total_price = Order.sum_order(data)

    context = {
        "user": user,
        "total_price": total_price
    }
    return render_template("orders/order_detail.html", **context)