"""Order controllers."""

# Flask
from flask import render_template, redirect, request, url_for, session, flash

# Config app
from app import app

# mercadopago
import mercadopago

# Models
from app.models.order import Order
from app.models.address import Address

@app.route("/pizzas/<int:pizza_id>/order/")
def add_order_pizza(pizza_id):
    """
    Agregar una pizza a las ordenes.
    """

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

    if "user" not in session:
        return redirect(url_for("index_register"))

    data = {"id": session['user']['id']}

    address = Address.get_one({"user_id": session["user"]["id"]})
    order_details = Order.get_orders_details(data)
    total_price = Order.sum_order_1(data)

    if request.method == "POST":
        data_add = {"user_id": session['user']['id']}
        Order.add_order_0(data_add)
        Order.delete_orders(data_add)
        return redirect(url_for("payment"))

    context = {
        "order_details": order_details,
        "total_price": total_price,
        "address": address,
        "count_pizzas": show_count_pizzas(data)
    }

    return render_template("orders/order_detail.html", **context)


@app.route("/orders/address", methods=["POST"])
def update_order_address():
    """
    Muestra la orden del usuario. deletable_1. y agrega a la ordenes pasadas. deletable_0
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
        return redirect(url_for("show_order"))

@app.route("/orders/payment/")
def payment():
    """
    Añade el método de pago (Mercado Pago).
    """
    
    if "user" not in session:
        return redirect(url_for("index_register"))

    data = {"id": session['user']['id']}

    total_price_data = Order.sum_order_0(data)
    total_price = int(total_price_data[0]["total_price"]) if total_price_data and total_price_data[0]["total_price"] else 0

    sdk = mercadopago.SDK("TEST-8024136192483870-072112-4fe0806e3c8a8b87ae5381289b424d5b-1429999768")
    preference_data = {
        "items": [
            {
                "title": "Total del pedido",
                "quantity": 1,
                "unit_price": total_price
            }
        ]
    }
    preference_response = sdk.preference().create(preference_data)
    preference = preference_response["response"]

    context = {
        "preference": preference,
        "total_price":total_price,
        "count_pizzas": show_count_pizzas(data)
        
    }
    print("Context:", context)
    return render_template("payment.html", **context)

def show_count_pizzas(data):
    """
    Muestra la cuenta de pizzas de la orden del usuario. deletable_1
    """
    
    count_pizzas = Order.get_count_pizzas(data)

    return count_pizzas
