"""User model."""

# Config
from app.config.mysql_connection import connect_to_mysql
from flask import flash

# Models
from app.models.pizza import Pizza

# the regex module
import re	
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    """Clase del modelo de usuario."""

    def __init__(self, data):
        """
        Constructor.

        El método `__init__()` es el constructor de la clase, se ejecuta cuando se crea
        una instancia de la clase. Las propiedades de la clase se definen en este método.

        Parámetros:
            self (object): Objeto de tipo `User`
            data (dict): Diccionario con los datos del usuario
        Retorna:
            None
        """

        self.id = data.get("id", 0)
        self.first_name = data.get("first_name", "")
        self.last_name = data.get("last_name", "")
        self.email = data.get("email", "")
        self.adress = data.get("adress", "")
        self.city = data.get("city", "")
        self.password = data.get("password", "")
        self.created_at = data.get("created_at", "")
        self.updated_at = data.get("updated_at", "")
        self.pizzas = []  # Lista de pizzas del usuario

    @classmethod
    def get_by_email(cls, data):
        """
        Obtener usuario por email.

        El método `get_by_email()` es un método de clase, lo que significa que se puede
        ejecutar sin crear una instancia de la clase.
        Ejemplo: User.get_by_email()

        Permite obtener un usuario por su email, con el fin de verificar si existe.

        Parámetros:
            cls (object): Objeto de tipo `User`
            data (dict): Diccionario con el email del usuario
        Retorna:
            user (object): Objeto de tipo `User`
        """
            
        query = """
        SELECT id, first_name, last_name, email, adress, city, password
        FROM users WHERE email = %(email)s;
        """
        results = connect_to_mysql().query_db(query, data)
    
        if results:
            return cls(results[0])
        return None
    
    @classmethod
    def register(cls, data):
        """
        Registro de usuario.

        El método `register()` es un método de clase, lo que significa que se puede
        ejecutar sin crear una instancia de la clase.
        Ejemplo: User.register()

        Permite registrar un usuario en la base de datos. Al registrar un usuario,
        se retorna el usuario registrado, mediante el método de clase `get_one()`.
        En caso de que no se registre el usuario, se retorna `None`.

        Parámetros:
            cls (object): Objeto de tipo `User`
            data (dict): Diccionario con los datos del usuario
        Retorna:
            user (object): Objeto de tipo `User`
        """

        query = """
        INSERT INTO users (first_name, last_name, email, adress, city, password, created_at, updated_at)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(adress)s, %(city)s, %(password)s, NOW(), NOW());
        """
        return connect_to_mysql().query_db(query, data)

    @classmethod #query
    def get_one(cls, data):
        """
        Obtener un usuario con sus pizzas.

        El método `get_one()` es un método de clase, lo que significa que se puede
        ejecutar sin crear una instancia de la clase.
        Ejemplo: User.get_one()

        Permite obtener un usuario por su ID, con el fin de obtener sus pizzas.

        Parámetros:
            cls (object): Objeto de tipo `User`
            data (dict): Diccionario con el ID del usuario
        Retorna:
            user (object): Objeto de tipo `User`
        """

        query = """
        SELECT * FROM users LEFT JOIN quotes
        ON users.id = quotes.user_id WHERE users.id = %(user_id)s;
        """
        results = connect_to_mysql().query_db(query, data)
        user = cls(results[0])
        for row in results:
            user.pizzas.append(Pizza(row))
        return user

    @staticmethod
    def validate_register(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connect_to_mysql().query_db(query,user)
        if len(results) >= 1:
            flash("Email ocupado.","danger")
            is_valid=False
        if not EMAIL_REGEX.match(user['email']):
            flash("Email invalido!!!","danger")
            is_valid=False
        if len(user['first_name']) < 3:
            flash("El nombre debe tener al menos 3 caracteres","danger")
            is_valid= False
        if len(user['password']) < 8:
            flash("La contraseña debe tener al menos 8 caracteres","danger")
            is_valid= False
        if user['password'] != user['password_confirm']:
            flash("Las contraseñas no coinciden","danger")
        return is_valid
    