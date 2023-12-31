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
        self.deletable = data.get("deletable", 1)
        self.created_at = data.get("created_at", "")
        self.updated_at = data.get("updated_at", "")

    @classmethod 
    def get_orders(cls, data):
        """
        Obtener todas las pizzas de la orden de un usuario. deletable_1
        """
        query = """
        SELECT orders.*, pizzas.*
        FROM orders
        JOIN pizzas ON orders.pizza_id = pizzas.id
        WHERE orders.user_id = %(id)s
        AND orders.deletable = 1;
        """
        order_pizzas = connect_to_mysql().query_db(query, data)
        return order_pizzas
    
    @classmethod
    def get_past_orders(cls, data):
        """
        Obtener las últimas órdenes pasadas creadas por el usuario. deletable_0
        """
        query = """
        SELECT orders.*, pizzas.*
        FROM orders
        JOIN pizzas ON orders.pizza_id = pizzas.id
        WHERE orders.user_id = %(id)s
        AND orders.deletable = 0;
        """
        order_past_pizzas = connect_to_mysql().query_db(query, data)
        return order_past_pizzas

    @classmethod
    def add_order_1(cls, data):
        """
        Agregar una pizza a la orden de un usuario. deletable_1
        """

        query = """
        INSERT INTO orders (pizza_id, user_id, deletable, created_at, updated_at)
        VALUES (%(pizza_id)s, %(user_id)s, 1, NOW(), NOW());
        """
        order_id = connect_to_mysql().query_db(query, data)
        return order_id

    @classmethod
    def add_order_0(cls, data):
        """
        Agrega todas las pizzas de la orden de un usuario. deletable_0
        """

        query = """
        INSERT INTO orders (pizza_id, user_id, deletable, created_at, updated_at)
        SELECT pizza_id, %(user_id)s, 0, NOW(), NOW()
        FROM orders
        WHERE deletable = 1;
        """
        order_id = connect_to_mysql().query_db(query, data)
        return order_id

    @classmethod
    def delete_order_1(cls, data):
        """
        Eliminar una pizza de la orden. deletable_1
        """
        query = """
        DELETE FROM orders WHERE pizza_id = %(pizza_id)s AND user_id = %(user_id)s AND deletable = 1;
        """
        return connect_to_mysql().query_db(query, data)
    
    @classmethod
    def delete_order_0(cls, data):
        """
        Eliminar una pizza de la orden. deletable_0
        """
        query = """
        DELETE FROM orders WHERE pizza_id = %(pizza_id)s AND user_id = %(user_id)s AND deletable = 0;
        """
        return connect_to_mysql().query_db(query, data)
    
    @classmethod
    def delete_orders(cls, data):
        """
        Eliminar todas las pizzas de la orden. deletable_1
        """
        query = """ 
        DELETE FROM orders WHERE deletable = 1 AND user_id = %(user_id)s;
        """
        return connect_to_mysql().query_db(query, data)
        
    @classmethod 
    def get_orders_details(cls, data):
        """
        Obtener todas las pizzas de la orden de un usuario. deletable_1
        """
        query = """
        SELECT orders.*, pizzas.*
        FROM orders
        JOIN pizzas ON orders.pizza_id = pizzas.id
        WHERE orders.user_id = %(id)s
        AND orders.deletable = 1;
        """
        order_details = connect_to_mysql().query_db(query, data)
        return order_details

    @classmethod
    def sum_order_1(cls, data):
        """
        Sumar todas las pizzas de la orden. deletable_1
        """
        query = """
        SELECT SUM(pizzas.price) AS total_price
        FROM users
        LEFT JOIN orders ON users.id = orders.user_id
        LEFT JOIN pizzas ON orders.pizza_id = pizzas.id
        WHERE users.id = %(id)s
        AND orders.deletable = 1;
        """
        total_price = connect_to_mysql().query_db(query, data)
        return total_price
    
    @classmethod
    def sum_order_0(cls, data): 
        """
        Sumar todas las pizzas de la orden, antes de dos minutos. deletable_0
        """
        query = """
        SELECT SUM(pizzas.price) AS total_price
        FROM users
        LEFT JOIN orders ON users.id = orders.user_id
        LEFT JOIN pizzas ON orders.pizza_id = pizzas.id
        WHERE users.id = %(id)s
        AND orders.deletable = 0
        AND orders.created_at >= DATE_SUB(NOW(), INTERVAL 2 MINUTE);
        """
        total_price = connect_to_mysql().query_db(query, data)
        return total_price
    
    @classmethod
    def get_count_pizzas(cls, data): 
        """
        Cuenta todas las pizzas de la orden del usuario. deletable_1
        """
        query = """
        SELECT COUNT(*) AS total_pizzas
        FROM orders
        WHERE orders.user_id = %(id)s
        AND orders.deletable = 1;
        """
        count_pizzas = connect_to_mysql().query_db(query, data)
        return count_pizzas[0]
