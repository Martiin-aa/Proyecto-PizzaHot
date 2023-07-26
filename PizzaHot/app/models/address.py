"""Address model."""

# Config
from app.config.mysql_connection import connect_to_mysql

# Models
from app.models.user import User

class Address:
    """Clase del modelo de direccion."""

    def __init__(self, data):
        """
        Constructor.
        """

        self.id = data.get("id", 0)
        self.district = data.get("district", "")
        self.address = data.get("address", "")
        self.house_number = data.get("house_number", 0)
        self.telephone = data.get("telephone", 0)
        self.user_id = data.get("user_id", 0)
        self.created_at = data.get("created_at", "")
        self.updated_at = data.get("updated_at", "")

    @classmethod 
    def update(cls, data):
        """
        Actualizar la direccion de un usuario si tiene una, sino la crea.
        """

        query = """
        INSERT INTO addresses (district, address, house_number, telephone, user_id, created_at, updated_at)
        VALUES (%(district)s, %(address)s, %(house_number)s, %(telephone)s, %(user_id)s, NOW(), NOW())
        ON DUPLICATE KEY UPDATE
        district = %(district)s, address = %(address)s, house_number = %(house_number)s, telephone = %(telephone)s;
        """
        return connect_to_mysql().query_db(query, data)
    
    @classmethod 
    def get_one(cls, data):
        """
        Obtener la dirreción del usuario por su ID.
        """

        query = """
        SELECT district, address, house_number, telephone
        FROM addresses
        WHERE user_id = %(user_id)s;
        """
        results = connect_to_mysql().query_db(query, data)
        return cls(results[0]) if results else None
    