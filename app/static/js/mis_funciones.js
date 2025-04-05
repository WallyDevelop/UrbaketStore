document.addEventListener('DOMContentLoaded', function () {
    let cantidad = 1;

    const cantidadBtn = document.getElementById("cantidadBtn");
    const incrementarBtn = document.getElementById("incrementarBtn");
    const decrementarBtn = document.getElementById("decrementarBtn");

    // Obtener el valor de stock desde el atributo data-unid-stock
    const stockDisponible = parseInt(document.getElementById("producto").getAttribute("data-unid-stock"));

    function actualizarCantidad() {
        cantidadBtn.textContent = "Cantidad: " + cantidad;
    }

    incrementarBtn.addEventListener("click", function () {
        if (cantidad < stockDisponible) {
            cantidad++;
            actualizarCantidad();
        }
    });

    decrementarBtn.addEventListener("click", function () {
        if (cantidad > 1) {
            cantidad--;
            actualizarCantidad();
        }
    });
});
