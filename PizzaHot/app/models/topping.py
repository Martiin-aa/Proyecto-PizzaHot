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
    def topping_pizza_create(cls, data):
        """
        Crea una nueva pizza que aumente el precio de la pizza original, 
        por cada topping agregado.
        """
        query = """
        INSERT INTO pizzas (name, size, crust, price, img, created_at, updated_at)
        SELECT CONCAT(pizzas.name, ' with ', GROUP_CONCAT(toppings.name SEPARATOR ', ')) AS name,
        pizzas.size,
        pizzas.crust,
        pizzas.price + SUM(toppings.price) AS price,
        pizzas.img,
        NOW() AS created_at,
        NOW() AS updated_at
        FROM pizzas
        JOIN pizzas_toppings ON pizzas.id = pizzas_toppings.pizza_id
        JOIN toppings ON toppings.id = pizzas_toppings.topping_id
        WHERE pizzas.id = %(pizza_id)s
        AND toppings.id IN %(topping_ids)s
        GROUP BY pizzas.id;
        """
        return connect_to_mysql().query_db(query, data)
    