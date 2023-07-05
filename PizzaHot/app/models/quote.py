"""Quote model."""

# Config
from app.config.mysql_connection import connect_to_mysql


class Quote:
    """Clase del modelo de cita."""

    def __init__(self, data) -> None:
        """
        Constructor.

        El método `__init__()` es el constructor de la clase, se ejecuta cuando se crea
        una instancia de la clase. Las propiedades de la clase se definen en este método.

        Parámetros:
            self (object): Objeto de tipo `Quote`
            data (dict): Diccionario con los datos de la cita
        Retorna:
            None
        """

        self.id = data["id"]
        self.author = data["author"]
        self.message = data["message"]
        self.user_id = data["user_id"]

    @classmethod
    def get_all(cls, data):
        """
        Obtener todas las citas sin favoritos de un usuario.

        El método `get_all()` es un método de clase, lo que significa que se puede
        ejecutar sin crear una instancia de la clase.
        Ejemplo: Quote.get_all()

        Parámetros:
            data (dict): Diccionario con el ID del usuario
        Retorna:
            quotes (list): Lista de citas sin favoritos
        """

        query = """
        SELECT quotes.id, quotes.author, quotes.message, quotes.user_id, users.name 
        FROM quotes 
        INNER JOIN users ON quotes.user_id = users.id
        WHERE quotes.id NOT IN (
            SELECT quote_id FROM favorites WHERE user_id = %(user_id)s  
        );
        """
        quotes = connect_to_mysql().query_db(query, data)
        return quotes
    
    @classmethod
    def get_one(cls, data):
        """
        Obtener una cita por ID.

        El método `get_one()` es un método de clase, lo que significa que se puede
        ejecutar sin crear una instancia de la clase.
        Ejemplo: Quote.get_one({"id": 1})

        Parámetros:
            cls (object): Objeto de tipo `Quote`
            data (dict): Diccionario con el ID de la cita
        Retorna:
            quote (object): Objeto de tipo `Quote`
        """

        query = """
        SELECT * FROM quotes WHERE id = %(quote_id)s;
        """
        quote = connect_to_mysql().query_db(query, data)
        return cls(quote[0])

    @classmethod
    def create(cls, data):
        """
        Crear una cita.

        El método `create()` es un método de clase, lo que significa que se puede
        ejecutar sin crear una instancia de la clase.
        Ejemplo: Quote.create({"author": "John Doe", "message": "Hello World", "user_id": 1})

        Parámetros:
            cls (object): Objeto de tipo `Quote`
            data (dict): Diccionario con los datos de la cita
        Retorna:
            quote_id (int): El ID de la cita creada
        """

        query = """
        INSERT INTO quotes (author, message, user_id)
        VALUES (%(author)s, %(message)s, %(user_id)s);  
        """
        quote_id = connect_to_mysql().query_db(query, data)
        return quote_id

    @classmethod
    def delete(cls, data):
        """
        Eliminar una cita.

        El método `delete()` es un método de clase, lo que significa que se puede
        llamar directamente desde la clase `Quote` sin necesidad de crear una instancia.
        Ejemplo: Quote.delete({"id": 1})

        Parámetros:
            cls (object): Objeto de tipo `Quote`
            data (dict): Diccionario con el ID de la cita
        Retorna:
            None
        """

        query = """
        DELETE FROM quotes WHERE id = %(quote_id)s;
        """
        return connect_to_mysql().query_db(query, data)

    @classmethod
    def update(cls, data):
        """
        Actualizar una cita.

        El método `update()` es un método de clase, lo que significa que se puede
        llamar directamente desde la clase `Quote` sin necesidad de crear una instancia.
        Ejemplo: Quote.update({"id": 1, "author": "John Doe", "message": "Hello World"})

        Parámetros:
            cls (object): Objeto de tipo `Quote`.
            data (dict): Diccionario con el ID de la cita, el autor y el mensaje.
        Retorna:
            None
        """

        query = """
        UPDATE quotes SET author = %(author)s, message = %(message)s WHERE id = %(quote_id)s;
        """
        return connect_to_mysql().query_db(query, data)

    @classmethod
    def get_number_of_quotes(cls, data):
        """
        Obtener el número de citas de un usuario.

        El método `get_number_of_quotes()` es un método de clase, lo que significa que se puede
        llamar directamente desde la clase `Quote` sin necesidad de crear una instancia.
        Ejemplo: Quote.get_number_of_quotes({"user_id": 1})

        Parámetros:
            cls (object): Objeto de tipo `Quote`.
            data (dict): Diccionario con el ID del usuario.
        Retorna:
            count (int): Número de citas de un usuario.
        """

        query = """
        SELECT COUNT(*) AS count FROM quotes WHERE user_id = %(user_id)s;
        """
        count = connect_to_mysql().query_db(query, data)
        return count[0]["count"]
