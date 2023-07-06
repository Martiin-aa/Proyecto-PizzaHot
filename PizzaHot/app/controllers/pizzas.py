"""Pizza controllers."""

# Flask
from flask import render_template, redirect, request, url_for, session

# Config app
from app import app

# Models
from app.models.pizza import Pizza
from app.models.order import Order


@app.route("/pizzas/")
def dashboard():
    """
    Página dashboard.

    La función `dashboard()` es una función de vista, lo que significa que se
    ejecuta cuando el usuario visita la ruta /pizzas/ en el navegador.
    Ejemplo: http://localhost:5000/pizzas/

    Parámetros:
        Ninguno
    Contexto:
        pizzas (list): Lista de pizzas no en la orden
        order_pizzas (list): Lista de pizzas en la orden
    Retorna:
        render_template: Renderiza la plantilla pizzas/dashboard.html
    """

    # Proteger la ruta /dashboard/
    if "user" not in session:
        return redirect(url_for("index"))

    # Obtener el ID del usuario de la sesión.
    data = {"user_id": session['user']['id']}

    pizzas = Pizza.get_all(data)
    order_pizzas = Order.get_orders(data)

    context = {
        "pizzas": pizzas,
        "order_pizzas": order_pizzas
    }
    return render_template("pizzas/dashboard.html", **context)


@app.route("/pizzas/<int:pizza_id>/order/")
def add_order_pizza(pizza_id):
    """
    Agregar una pizza a las ordenes.

    La función `add_favorite_pizza()` es una función de vista, lo que significa que se
    ejecuta cuando el usuario da clic en el botón agregar una pizza a la orden.
    Ejemplo: http://localhost:5000/pizzas/1/order/

    Parámetros:
        pizza_id (int): ID de la pizza
    Retorna:
        redirect: Redirecciona a la función `dashboard()`
    """

    # Proteger la ruta /pizzas/<int:pizza_id>/order/
    if "user" not in session:
        return redirect(url_for("index"))

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

    La función `remove_order_pizza()` es una función de vista, lo que significa que se
    ejecuta cuando el usuario da clic en el botón remover una pizza de la orden.
    Ejemplo: http://localhost:5000/pizzas/1/remove/

    Parámetros:
        pizza_id (int): ID de la pizza
    Retorna:
        redirect: Redirecciona a la función `dashboard()`
    """

    # Proteger la ruta /pizzas/<int:pizza_id>/remove/
    if "user" not in session:
        return redirect(url_for("index"))

    data = {
        "pizza_id": pizza_id,
        "user_id": session['user']['id']
    }
    Order.delete(data)
    return redirect(url_for("dashboard"))


@app.route("/pizzas/<int:pizza_id>/delete/")
def delete_pizza(pizza_id):
    """
    Eliminar una pizza.

    La función `delete_pizza()` es una función de vista, lo que significa que se
    ejecuta cuando el usuario da clic en el botón eliminar una pizza.
    Ejemplo: http://localhost:5000/pizzas/1/delete/

    Parámetros:
        pizza_id (int): ID de la cita
    Retorna:
        redirect: Redirecciona a la función `dashboard()`
    """

    # Proteger la ruta /pizzas/<int:pizza_id>/delete/
    if "user" not in session:
        return redirect(url_for("index"))

    data = {"pizza_id": pizza_id}
    Pizza.delete(data)
    return redirect(url_for("dashboard"))


@app.route("/pizzas/create/", methods=["POST"]) #data
def create_pizza():
    """
    Crear una pizza.

    La función `create_pizza()` es una función de vista, lo que significa que se
    ejecuta cuando el usuario da clic en el botón crear una cita.
    Ejemplo: http://localhost:5000/pizzas/create/

    Parámetros:
        Ninguno
    Retorna:
        redirect: Redirecciona a la función `dashboard()`
    """

    # Proteger la ruta /pizzas/create/
    if "user" not in session:
        return redirect(url_for("index"))

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

    La función `update_pizza()` es una función de vista, lo que significa que se
    ejecuta cuando el usuario da clic en el botón actualizar una pizza.
    Ejemplo: http://localhost:5000/pizzas/1/

    Parámetros:
        pizza_id (int): ID de la pizza
    Retorna:
        redirect: Redirecciona a la función `dashboard()`
    """

    # Proteger la ruta /pizzas/<int:pizza_id>/
    if "user" not in session:
        return redirect(url_for("index"))

    # Diccionario
    data = {"pizza_id": pizza_id}
    pizza = Pizza.get_one(data)

    if request.method == "POST":
        data = {
            "pizza_id": pizza_id,
            "name": request.form['name'],
            "size": request.form['size'],
            "crust": request.form['crust']
        }
        Pizza.update(data)
        return redirect(url_for("dashboard"))
    return render_template("pizzas/pizza_update.html", pizza=pizza)
