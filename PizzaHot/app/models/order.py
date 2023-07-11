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
        self.pizza_id = data.get("pizza_id", 0)
        self.user_id = data.get("user_id", 0)
        self.created_at = data.get("created_at", "")
        self.updated_at = data.get("updated_at", "")

    @classmethod 
    def get_orders(cls, data):
        """
        Obtener todas las pizzas de la orden de un usuario.
        """
        query = """
        SELECT orders.*, pizzas.*
        FROM orders
        JOIN pizzas ON orders.pizza_id = pizzas.id
        WHERE orders.user_id = %(id)s;
        """
        order_pizzas = connect_to_mysql().query_db(query, data)
        return order_pizzas
    
    @classmethod
    def get_past_orders(cls, data):
        """
        Obtener todas las ordenes pasadas creadas por el usuario. luego de 30 min o mas. 
        """
        query = """
        SELECT orders.*, pizzas.*
        FROM orders
        JOIN users ON orders.user_id = users.id 
        JOIN pizzas ON orders.pizza_id = pizzas.id
        WHERE users.id = %(id)s
        AND orders.created_at <= TIMESTAMPADD(MINUTE, -30, NOW());
        """
        order_past_pizzas = connect_to_mysql().query_db(query, data)
        return order_past_pizzas

    @classmethod
    def add_order(cls, data):
        """
        Agregar una pizza a la orden de un usuario.
        """

        query = """
        INSERT INTO orders (pizza_id, user_id, created_at, updated_at)
        VALUES (%(pizza_id)s, %(user_id)s, NOW(), NOW());
        """
        order_id = connect_to_mysql().query_db(query, data)
        return order_id

    @classmethod
    def delete_order(cls, data):
        """
        Eliminar una pizza de la orden.
        """
        query = """
        DELETE FROM orders WHERE pizza_id = %(pizza_id)s AND user_id = %(user_id)s;
        """
        return connect_to_mysql().query_db(query, data)
    
    @classmethod 
    def get_orders_details(cls, data):
        """
        Obtener todas las pizzas de la orden de un usuario.
        """
        query = """
        SELECT orders.*, pizzas.*
        FROM orders
        JOIN pizzas ON orders.pizza_id = pizzas.id
        WHERE orders.user_id = %(id)s;
        """
        order_details = connect_to_mysql().query_db(query, data)
        return order_details

    @classmethod
    def sum_order(cls, data): 
        """
        Sumar todas las pizzas de la orden.
        """
        query = """
        SELECT users.id, users.first_name, users.last_name, SUM(pizzas.price) AS total_price
        FROM users
        LEFT JOIN orders ON users.id = orders.user_id
        LEFT JOIN pizzas ON orders.pizza_id = pizzas.id
        GROUP BY users.id, users.first_name, users.last_name
        HAVING users.id = %(id)s;
        """
        total_price = connect_to_mysql().query_db(query, data)
        return total_price