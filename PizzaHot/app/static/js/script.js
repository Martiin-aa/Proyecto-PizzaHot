// Pagar
function mostrarAlerta() {
    var opcionesPago = {
        1: "Crédito",
        2: "Transferencia",
        3: "Efectivo"
    };

    var metodoPago = prompt("Seleccione el método de pago:\n\n1. Crédito\n2. Transferencia\n3. Efectivo");
    if (metodoPago && opcionesPago[metodoPago]) {
        var confirmacion = confirm("¿Estás seguro de que quieres confirmar el pago?\n\nMétodo de Pago: " + opcionesPago[metodoPago] + "\nTotal a Pagar: " + document.getElementById("total_price").value);
        if (confirmacion) {
            alert("¡Pago confirmado!");
        }
    }
}



