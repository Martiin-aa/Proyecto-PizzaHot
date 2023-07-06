"""Pizza model."""

# Config
from app.config.mysql_connection import connect_to_mysql


class Pizza:
    """Clase del modelo de pizza."""

    def __init__(self, data) -> None:
        """
        Constructor.

        El método `__init__()` es el constructor de la clase, se ejecuta cuando se crea
        una instancia de la clase. Las propiedades de la clase se definen en este método.

        Parámetros:
            self (object): Objeto de tipo `Pizza`
            data (dict): Diccionario con los datos de la pizza
        Retorna:
            None
        """

        self.id = data["id"]
        self.name = data["name"]
        self.size = data["size"]
        self.crust = data["crust"]
        self.price = data["price"]

    @classmethod #query
    def get_all(cls, data):
        """
        Obtener todas las pizzas sin estar en la orden de un usuario.

        El método `get_all()` es un método de clase, lo que significa que se puede
        ejecutar sin crear una instancia de la clase.
        Ejemplo: Pizza.get_all()

        Parámetros:
            data (dict): Diccionario con el ID del usuario
        Retorna:
            quotes (list): Lista de pizzas sin estar en alguna orden
        """

        query = """
        SELECT quotes.id, quotes.author, quotes.message, quotes.user_id, users.name 
        FROM quotes 
        INNER JOIN users ON quotes.user_id = users.id
        WHERE quotes.id NOT IN (
            SELECT quote_id FROM favorites WHERE user_id = %(user_id)s  
        );
        """
        pizzas = connect_to_mysql().query_db(query, data)
        return pizzas
    
    @classmethod #query
    def get_one(cls, data):
        """
        Obtener una pizza por ID.

        El método `get_one()` es un método de clase, lo que significa que se puede
        ejecutar sin crear una instancia de la clase.
        Ejemplo: Pizza.get_one({"id": 1})

        Parámetros:
            cls (object): Objeto de tipo `Pizza`
            data (dict): Diccionario con el ID de la pizza
        Retorna:
            quote (object): Objeto de tipo `Pizza`
        """

        query = """
        SELECT * FROM quotes WHERE id = %(quote_id)s;
        """
        pizza = connect_to_mysql().query_db(query, data)
        return cls(pizza[0])

    @classmethod #query
    def create(cls, data):
        """
        Crear una pizza.

        El método `create()` es un método de clase, lo que significa que se puede
        ejecutar sin crear una instancia de la clase.
        Ejemplo: Pizza.create({"name": "peperonni", "size": "large", "crust": "slim", "price: "1.220"})

        Parámetros:
            cls (object): Objeto de tipo `Pizza`
            data (dict): Diccionario con los datos de la pizza
        Retorna:
            quote_id (int): El ID de la pizza creada
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

        El método `delete()` es un método de clase, lo que significa que se puede
        llamar directamente desde la clase `Pizza` sin necesidad de crear una instancia.
        Ejemplo: Pizza.delete({"id": 1})

        Parámetros:
            cls (object): Objeto de tipo `Pizza`
            data (dict): Diccionario con el ID de la pizza
        Retorna:
            None
        """

        query = """
        DELETE FROM quotes WHERE id = %(quote_id)s;
        """
        return connect_to_mysql().query_db(query, data)

    @classmethod #query
    def update(cls, data):
        """
        Actualizar una pizza.

        El método `update()` es un método de clase, lo que significa que se puede
        llamar directamente desde la clase `Pizza` sin necesidad de crear una instancia.
        Ejemplo: Pizza.update({"id": 1, "name": "peperonni", "size": "large", "crust": "slim", "price: "1.220""})

        Parámetros:
            cls (object): Objeto de tipo `Pizza`.
            data (dict): Diccionario con el ID de la pizza, el nombre, tamaño, masa y precio.
        Retorna:
            None
        """

        query = """
        UPDATE quotes SET author = %(author)s, message = %(message)s WHERE id = %(quote_id)s;
        """
        return connect_to_mysql().query_db(query, data)

    @classmethod #query
    def get_number_of_pizzas(cls, data):
        """
        Obtener el número de pizzas de el usuario.

        El método `get_number_of_pizzas()` es un método de clase, lo que significa que se puede
        llamar directamente desde la clase `Pizza` sin necesidad de crear una instancia.
        Ejemplo: Pizza.get_number_of_quotes({"user_id": 1})

        Parámetros:
            cls (object): Objeto de tipo `Pizza`.
            data (dict): Diccionario con el ID del usuario.
        Retorna:
            count (int): Número de pizzas de un usuario.
        """

        query = """
        SELECT COUNT(*) AS count FROM quotes WHERE user_id = %(user_id)s;
        """
        count = connect_to_mysql().query_db(query, data)
        return count[0]["count"]
