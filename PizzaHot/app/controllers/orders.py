"""Order controllers."""

# Flask
from flask import render_template, redirect, request, url_for, session, flash

# Config app
from app import app

# SDK de Mercado Pago
import mercadopago
sdk = mercadopago.SDK("TEST-8024136192483870-072112-4fe0806e3c8a8b87ae5381289b424d5b-1429999768")

# Models
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

@app.route("/orders/detail", methods=["GET", "POST"])
def show_order():
    """
    Muestra la orden del usuario. deletable_1. y agrega a la ordenes pasadas. deletable_0
    """

    # Proteger la ruta /orders/detail
    if "user" not in session:
        return redirect(url_for("index_register"))

    data = {"id": session['user']['id']}

    order_details = Order.get_orders_details(data)
    total_price = Order.sum_order(data)

    if request.method == "POST":
        data_add = {"user_id": session['user']['id']}
        Order.add_order_0(data_add)
        return redirect(url_for("payment"))

    context = {
        "order_details": order_details,
        "total_price": total_price,
        "count_pizzas": show_count_pizzas(data)
    }

    return render_template("orders/order_detail.html", **context)

@app.route("/orders/payment", methods=["GET", "POST"])
def payment():
    """
    Añade el metodo de pago (mercado pago).
    """
    # Proteger la ruta /orders/payment
    if "user" not in session:
        return redirect(url_for("index_register"))
    
    data = {"id": session['user']['id']}
    preference = None

    if request.method == "POST":
        # Crea un ítem en la preferencia
        preference_data = {
            "items": [
                {
                    "title": "Mi producto",
                    "quantity": 1,
                    "unit_price": 75
                }
            ]
        }
        preference_response = sdk.preference().create(preference_data)
        preference = preference_response["response"]
        flash("!Pago realizado!", "success")
        return redirect(url_for("dashboard"))
    
    context = {
        "count_pizzas": show_count_pizzas(data),
        "preference": preference
    }

    return render_template("payment.html", **context)

def show_count_pizzas(data):
    """
    Muestra la cuenta de pizzas de la orden del usuario. deletable_1
    """
    
    count_pizzas = Order.get_count_pizzas(data)

    return count_pizzas
