"""Server."""

# App config
from app import app

# Controllers
from app.controllers.users import *
from app.controllers.pizzas import *


# Run
if __name__ == "__main__":
    app.run(debug=True)
