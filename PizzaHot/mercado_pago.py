# SDK de Mercado Pago
import mercadopago

# Agrega credenciales
sdk = mercadopago.SDK("TEST-8024136192483870-072112-4fe0806e3c8a8b87ae5381289b424d5b-1429999768")

# Ejemplo: obtener información del usuario autenticado
user_info = sdk.get("/users/me")
print(user_info)

# Crea un ítem en la preferencia
preference_data = {
    "items": [
        {
            "title": "Mi producto",
            "quantity": 1,
            "unit_price": 75
        }
    ]
}

preference_response = sdk.preference().create(preference_data)
preference = preference_response["response"]
