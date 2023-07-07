"""Order model."""

# Config
from app.config.mysql_connection import connect_to_mysql


class Order:
    """Clase del modelo de ordenes."""

    def __init__(self, data) -> None:
        """
        Constructor.
        """

        self.id = data.get("id", 0)
        self.price = data.get("price", 0)
        self.pizza_id = data.get("pizza_id", 0)
        self.user_id = data.get("user_id", 0)
        self.created_at = data.get("created_at", "")
        self.updated_at = data.get("updated_at", "")

    @classmethod #query
    def get_orders(cls, data):
        """
        Obtener todas las pizzas de la orden de un usuario.
        """
        query = """
            SELECT pizzas.*
            FROM pizzas
            JOIN orders ON pizzas.id = orders.pizza_id
            WHERE orders.user_id = %(id)s;
            """
        order_pizzas = connect_to_mysql().query_db(query, data)
        return order_pizzas
    
    @classmethod
    def get_past_orders(cls, data):
        """
        Obtener todas las ordenes pasadas creadas por el usuario.
        """
        query = """
            SELECT orders.*
            FROM orders
            JOIN users ON orders.user_id = users.id
            WHERE users.id = %(id)s
            AND orders.created_at < NOW();
            """
        order_past_pizzas = connect_to_mysql().query_db(query, data)
        return order_past_pizzas

    @classmethod
    def add_order(cls, data):
        """
        Agregar una pizza a la orden de un usuario.
        """

        query = """
        INSERT INTO orders (pizza_id, user_id)
        VALUES (%(pizza_id)s, %(user_id)s);
        """
        order_id = connect_to_mysql().query_db(query, data)
        return order_id

    @classmethod
    def delete(cls, data):
        """
        Eliminar una pizza de la orden.
        """
        query = """
        DELETE FROM orders WHERE pizza_id = %(pizza_id)s AND user_id = %(user_id)s;
        """
        return connect_to_mysql().query_db(query, data)
