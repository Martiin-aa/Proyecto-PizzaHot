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
        """

        self.id = data.get("id", 0)
        self.first_name = data.get("first_name", "")
        self.last_name = data.get("last_name", "")
        self.email = data.get("email", "")
        self.password = data.get("password", "")
        self.logo = data.get("logo", "")
        self.created_at = data.get("created_at", "")
        self.updated_at = data.get("updated_at", "")
        self.pizzas = []  # Lista de pizzas del usuario

    @classmethod
    def get_by_email(cls, data):
        """
        Obtener usuario por email.
        """

        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connect_to_mysql().query_db(query, data)
        if results:
            return cls(results[0])
        return None
    
    @classmethod
    def register(cls, data):
        """
        Registro de usuario.
        """

        query = """
        INSERT INTO users (first_name, last_name, email, password, created_at, updated_at)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());
        """

        results = connect_to_mysql().query_db(query, data)
    
        if results:
            user_data = {
                "id": results,
                "first_name": data["first_name"],
                "last_name": data["last_name"],
                "email": data["email"]
            }
            return cls(user_data)

        return None
    
    @classmethod 
    def update(cls, data):
        """
        Actualizar un usuario.
        """

        query = """
        UPDATE users
        SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s
        WHERE id = %(user_id)s;
        """
        return connect_to_mysql().query_db(query, data)

    @classmethod 
    def get_one(cls, data):
        """
        Obtener un usuario.
        """

        query = """
        SELECT * FROM users WHERE id = %(id)s;
        """
        user = connect_to_mysql().query_db(query, data)
        return cls(user[0])
    
    
    @classmethod
    def get_by_id(cls,data):
        """
        Obtener un usuario por su id.
        """
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connect_to_mysql().query_db(query, data)
        if results:
            return cls(results[0])
        return None
    
    @classmethod 
    def update_photo(cls, data):
        """
        Actualizar la foto de perfil de un usuario.
        """

        query = """
        UPDATE users
        SET logo = %(logo)s
        WHERE id = %(user_id)s;
        """
        return connect_to_mysql().query_db(query, data)

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
