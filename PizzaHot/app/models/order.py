"""Order model."""

# Config
from app.config.mysql_connection import connect_to_mysql


class Order:
    """Clase del modelo de ordenes."""

    def __init__(self, data) -> None:
        """
        Constructor.

        El método `__init__()` es el constructor de la clase, se ejecuta cuando se crea
        una instancia de la clase. Las propiedades de la clase se definen en este método.

        Parámetros:
            self (object): Objeto de tipo `Order`
            data (dict): Diccionario con los datos de la orden
        Retorna:
            None
        """

        self.id = data["id"]
        self.pizza_id = data["pizza_id"]
        self.user_id = data["user_id"]

    @classmethod #query
    def get_orders(cls, data):
        """
        Obtener todas las pizzas de la orden de un usuario.

        El método `get_orders()` es un método de clase, lo que significa que se puede
        llamar directamente desde la clase `Order` sin necesidad de crear una instancia.
        Ejemplo: Order.get_orders({"id": 1})

        Parámetros:
            cls (object): Objeto de tipo `Order`
            data (dict): Diccionario con el ID del usuario
        Retorna:
            favorites_quotes (list): Lista de pizzas en la orden
        """
        query = """
            SELECT 
                favorites.id, favorites.user_id AS favorites_user_id, favorites.quote_id, 
                quotes.user_id AS quotes_user_id, quotes.message, users.name 
            FROM favorites
            INNER JOIN quotes ON favorites.quote_id = quotes.id
            INNER JOIN users ON quotes.user_id = users.id
            WHERE favorites.user_id = %(user_id)s;
            """
        order_pizzas = connect_to_mysql().query_db(query, data)
        return order_pizzas

    @classmethod
    def add_order(cls, data):
        """
        Agregar una pizza a la orden de un usuario.

        El método `add_order()` es un método de clase, lo que significa que se puede
        llamar directamente desde la clase `Order` sin necesidad de crear una instancia.
        Ejemplo: Order.add_order({"pizza_id": 1, "user_id": 1})

        Parámetros:
            cls (object): Objeto de tipo `Pizza`
            data (dict): Diccionario con el ID de la pizza y el ID del usuario
        Retorna:
            order_id (int): El ID de la pizza agregada a la orden
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

        El método `delete_order()` es un método de clase, lo que significa que se puede
        llamar directamente desde la clase `Pizza` sin necesidad de crear una instancia.
        Ejemplo: Pizza.delete_order({"pizza_id": 1, "user_id": 1})

        Parámetros:
            cls (object): Objeto de tipo `Pizza`
            data (dict): Diccionario con el ID de la pizza y el ID del usuario
        Retorna:
            None
        """
        query = """
        DELETE FROM orders WHERE pizza_id = %(pizza_id)s AND user_id = %(user_id)s;
        """
        return connect_to_mysql().query_db(query, data)
