"""Topping model."""

# Config
from app.config.mysql_connection import connect_to_mysql


class Topping:
    """Clase del modelo de aderezos."""

    def __init__(self, data):
        """
        Constructor.
        """

        self.id = data.get("id", 0)
        self.name = data.get("name", "")
        self.price = data.get("price", 0)
        self.created_at = data.get("created_at", "")
        self.updated_at = data.get("updated_at", "")

    @classmethod 
    def get_all(cls, data):
        """
        Obtener todas los aderezos disponibles.
        """

        query = """
        SELECT * FROM toppings;
        """
        toppings = connect_to_mysql().query_db(query, data)
        return toppings
    
    @classmethod 
    def topping_order_update(cls, data):
        """
        Se actualiza el precio de cada pizza, por cada topping seleccionado.
        """
        query = """
        UPDATE pizzas
        SET price = price + (
        SELECT SUM(toppings.price)
        FROM toppings
        JOIN toppings_pizzas ON toppings.id = toppings_pizzas.topping_id
        WHERE toppings_pizzas.pizza_id = pizzas.id
        );
        """
        return connect_to_mysql().query_db(query, data)