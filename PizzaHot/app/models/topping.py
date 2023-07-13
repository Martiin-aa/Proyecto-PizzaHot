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
    def get_all(cls):
        """
        Obtener todas los aderezos disponibles.
        """

        query = """
        SELECT * FROM toppings;
        """
        toppings = connect_to_mysql().query_db(query)
        return toppings
    
    @classmethod
    def get_toppings_by_pizza(cls, data):
        """
        Obtener los aderezos asociados a una pizza específica.
        """
        query = """
        SELECT toppings.*
        FROM toppings
        JOIN toppings_pizzas ON toppings.id = toppings_pizzas.topping_id
        WHERE toppings_pizzas.pizza_id = %(pizza_id)s;
        """
    
        toppings = connect_to_mysql().query_db(query, data)
        return toppings
    