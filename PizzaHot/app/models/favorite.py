"""Favorite model."""

# Config
from app.config.mysql_connection import connect_to_mysql


class Favorite:
    """Clase del modelo de favoritos."""

    def __init__(self, data) -> None:
        """
        Constructor.

        El método `__init__()` es el constructor de la clase, se ejecuta cuando se crea
        una instancia de la clase. Las propiedades de la clase se definen en este método.

        Parámetros:
            self (object): Objeto de tipo `Favorite`
            data (dict): Diccionario con los datos del favorito
        Retorna:
            None
        """

        self.id = data["id"]
        self.user_id = data["user_id"]
        self.quote_id = data["quote_id"]

    @classmethod
    def get_favorites(cls, data):
        """
        Obtener todas las citas favoritas de un usuario.

        El método `get_favorites()` es un método de clase, lo que significa que se puede
        llamar directamente desde la clase `Quote` sin necesidad de crear una instancia.
        Ejemplo: Quote.get_favorites({"id": 1})

        Parámetros:
            cls (object): Objeto de tipo `Quote`
            data (dict): Diccionario con el ID del usuario
        Retorna:
            favorites_quotes (list): Lista de citas favoritas
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
        favorite_quotes = connect_to_mysql().query_db(query, data)
        return favorite_quotes

    @classmethod
    def add_favorite(cls, data):
        """
        Agregar una cita a favoritos a un usuario.

        El método `add_favorite()` es un método de clase, lo que significa que se puede
        llamar directamente desde la clase `Quote` sin necesidad de crear una instancia.
        Ejemplo: Quote.add_favorite({"quote_id": 1, "user_id": 1})

        Parámetros:
            cls (object): Objeto de tipo `Quote`
            data (dict): Diccionario con el ID de la cita y el ID del usuario
        Retorna:
            favorite_id (int): El ID de la cita agregada a favoritos
        """

        query = """
        INSERT INTO favorites (quote_id, user_id)
        VALUES (%(quote_id)s, %(user_id)s);
        """
        favorite_id = connect_to_mysql().query_db(query, data)
        return favorite_id

    @classmethod
    def delete(cls, data):
        """
        Eliminar una cita de favoritos.

        El método `delete_favorite()` es un método de clase, lo que significa que se puede
        llamar directamente desde la clase `Quote` sin necesidad de crear una instancia.
        Ejemplo: Quote.delete_favorite({"quote_id": 1, "user_id": 1})

        Parámetros:
            cls (object): Objeto de tipo `Quote`
            data (dict): Diccionario con el ID de la cita y el ID del usuario
        Retorna:
            None
        """
        query = """
        DELETE FROM favorites WHERE quote_id = %(quote_id)s AND user_id = %(user_id)s;
        """
        return connect_to_mysql().query_db(query, data)
