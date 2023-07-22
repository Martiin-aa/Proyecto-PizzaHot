// Pagar modal
function mostrarAlerta() {
    var opcionesPago = {
        1: "Crédito",
        2: "debito"
    };

    var metodoPago = prompt("Seleccione una de las opciones de pago de Mercado Pago:\n1. Crédito\n2. debito");
    if (metodoPago && opcionesPago[metodoPago]) {
        var confirmacion = confirm("¿Estás seguro de que quieres confirmar el pago?\n\nMétodo de Pago: " + opcionesPago[metodoPago] + "\nTotal a Pagar: " + document.getElementById("total_price").value);
    }
}

// Mercado pago
const mp = new MercadoPago('TEST-b61b00ab-80b9-4ab9-8381-d19839e3b8d5');
const bricksBuilder = mp.bricks();

const preferenceId = preference.id;

mp.bricks().create("wallet", "wallet_container", {
    initialization: {
        preferenceId: preferenceId,
    },
});
