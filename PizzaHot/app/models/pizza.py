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
        self.deletable = data.get("deletable", 1)
        self.topping_id = data.get("topping_id", 0)
        self.created_at = data.get("created_at", "")
        self.updated_at = data.get("updated_at", "")

    @classmethod 
    def get_all(cls, data):
        """
        Obtener todas las pizzas sin estar en la orden de un usuario, y tengan un id igual o menor a 9. deletable_1
        """

        query = """
        SELECT *
        FROM pizzas
        WHERE id <= 9
        AND id NOT IN (
        SELECT pizza_id
        FROM orders
        WHERE user_id = %(id)s
        AND orders.deletable = 1
        );
        """
        pizzas = connect_to_mysql().query_db(query, data)
        return pizzas
    
    @classmethod 
    def get_one(cls, data):
        """
        Obtener una pizza por ID.
        """

        query = """
        SELECT * FROM pizzas WHERE id = %(pizza_id)s;
        """
        pizza = connect_to_mysql().query_db(query, data)
        return cls(pizza[0])
    
    @classmethod 
    def create(cls, data):
        """
        Crear una pizza. con la suma de los toppings seleccionados en el precio de la pizza.
        """

        query = """
        INSERT INTO pizzas (name, size, crust, price, img, created_at, updated_at)
        VALUES (%(name)s, %(size)s, %(crust)s, %(price)s + (
        SELECT SUM(toppings.price)
        FROM toppings
        WHERE toppings.id IN %(topping_ids)s
        ), %(img)s, NOW(), NOW());
        """
        pizza_id = connect_to_mysql().query_db(query, data)
        return pizza_id

    @classmethod 
    def delete(cls, data):
        """
        Eliminar una pizza.
        """

        query = """
        DELETE FROM pizzas WHERE id = %(id)s;
        """
        return connect_to_mysql().query_db(query, data)

    @classmethod 
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

