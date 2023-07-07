"""Pizza model."""

# Config
from app.config.mysql_connection import connect_to_mysql


class Pizza:
    """Clase del modelo de pizza."""

    def __init__(self, data) -> None:
        """
        Constructor.
        """

        self.id = data.get("id", 0)
        self.name = data.get("name", "")
        self.size = data.get("size", "")
        self.crust = data.get("crust", "")
        self.price = data.get("price", 0)
        self.img = data.get("img", "")
        self.created_at = data.get("created_at", "")
        self.updated_at = data.get("updated_at", "")

    @classmethod #query
    def get_all(cls, data):
        """
        Obtener todas las pizzas sin estar en la orden de un usuario.
        """

        query = """
        SELECT *
        FROM pizzas
        WHERE id NOT IN (
        SELECT pizza_id
        FROM orders
        WHERE user_id = %(id)s
        );
        """
        pizzas = connect_to_mysql().query_db(query, data)
        return pizzas
    
    @classmethod #query
    def get_one(cls, data):
        """
        Obtener una pizza por ID.
        """

        query = """
        SELECT * FROM pizzas WHERE id = %(id)s;
        """
        pizza = connect_to_mysql().query_db(query, data)
        return cls(pizza[0])

    @classmethod #query
    def create(cls, data):
        """
        Crear una pizza.
        """

        query = """
        INSERT INTO quotes (author, message, user_id)
        VALUES (%(author)s, %(message)s, %(user_id)s);  
        """
        pizza_id = connect_to_mysql().query_db(query, data)
        return pizza_id

    @classmethod #query
    def delete(cls, data):
        """
        Eliminar una pizza.
        """

        query = """
        DELETE FROM pizzas WHERE id = %(id)s;
        """
        return connect_to_mysql().query_db(query, data)

    @classmethod #query
    def update(cls, data):
        """
        Actualizar una pizza.
        """

        query = """
        UPDATE pizzas
        SET name = %(name)s, size = %(size)s, crust = %(crust)s, price = %(price)s
        WHERE id = %(id)s;
        """
        return connect_to_mysql().query_db(query, data)

    @classmethod #query
    def get_number_of_pizzas(cls, data):
        """
        Obtener el número de pizzas de el usuario.
        """

        query = """
        SELECT COUNT(*) AS count FROM quotes WHERE user_id = %(user_id)s;
        """
        count = connect_to_mysql().query_db(query, data)
        return count[0]["count"]