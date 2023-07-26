// Pagar modal pagina order_detail 
function mostrarAlerta() {
    var opcionesPago = {
        1: "Crédito",
        2: "debito"
    };

    var metodoPago = prompt("Seleccione una de las opciones de pago de Mercado Pago:\n1. Crédito\n2. debito");
    if (metodoPago && opcionesPago[metodoPago]) {
        var confirmacion = confirm("¿Estás seguro ir a cancelar la orden?\n\nMétodo de Pago: " + opcionesPago[metodoPago] + "\nTotal a Pagar: " + document.getElementById("total_price").value);
    }
}
