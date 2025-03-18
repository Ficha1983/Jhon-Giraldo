<?php
while (true) {
    echo "Introduzca un valor mayor a 10: ";
    $a = (int) fgets(STDIN);  // Lee la entrada del usuario

    if ($a > 10) {
        echo "Es correcto<br>";
    } else {
        echo "Es incorrecto, pruebe de nuevo<br>";
        break; // Sale del bucle si el valor no es mayor a 10
    }
}
?>
