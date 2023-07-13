"""Order controllers."""

# Flask
from flask import render_template, redirect, request, url_for, session

# Config app
from app import app

# Models
from app.models.user import User
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
    Order.add_order_1(data)
    Order.add_order_0(data)
    return redirect(url_for("dashboard"))

@app.route("/pizzas/<int:pizza_id>/remove_1/")
def remove_order_pizza_1(pizza_id):
    """
    Eliminar una pizza de la orden. deletable_1
    """

    # Proteger la ruta /pizzas/<int:pizza_id>/remove/
    if "user" not in session:
        return redirect(url_for("index_register"))

    data = {
        "pizza_id": pizza_id,
        "user_id": session['user']['id']
    }
    Order.delete_order_1(data)
    return redirect(url_for("dashboard"))

@app.route("/pizzas/<int:pizza_id>/remove_0/")
def remove_order_pizza_0(pizza_id):
    """
    Eliminar una pizza de la orden. deletable_0
    """

    # Proteger la ruta /pizzas/<int:pizza_id>/remove/
    if "user" not in session:
        return redirect(url_for("index_register"))

    data = {
        "pizza_id": pizza_id,
        "user_id": session['user']['id']
    }
    Order.delete_order_0(data)
    return redirect(url_for("dashboard"))

@app.route("/orders/detail")
def show_order():
    """
    Muestra la orden del usuario. deletable_1
    """

    # Proteger la ruta /orders/
    if "user" not in session:
        return redirect(url_for("index_register"))

    data = {"id": session['user']['id']}

    order_details = Order.get_orders_details(data)
    total_price = Order.sum_order(data)

    context = {
        "order_details": order_details,
        "total_price": total_price
    }
    return render_template("orders/order_detail.html", **context)