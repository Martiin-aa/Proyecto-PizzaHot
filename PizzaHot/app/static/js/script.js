// Pagar modal pagina order_detail 
function mostrarAlerta() {
    var totalPagar = document.getElementById("total_price").value;
    if (totalPagar) {
        confirm("¿Estás seguro de ir a cancelar la orden?\n\nTotal a Pagar: " + totalPagar);
    }
}
