"""Server."""

# App config
from app import app

# Controllers
from app.controllers.users import *
from app.controllers.pizzas import *
from app.controllers.orders import *

# Run
if __name__ == "__main__":
    app.run(debug=True)

