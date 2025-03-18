<?php
// Solicitar al usuario que ingrese el valor del voltaje y la resistencia
echo "Ingrese el valor del voltaje del circuito: ";
$voltaje = (int)trim(fgets(STDIN));  // Leemos el voltaje y lo convertimos a entero

echo "Ingrese el valor de la resistencia del circuito: ";
$resistencia = (int)trim(fgets(STDIN));  // Leemos la resistencia y la convertimos a entero

// Calculamos la intensidad (amperaje) utilizando la fórmula de Ohm
$intensidad = $voltaje / $resistencia;

// Imprimir el resultado
echo "Al conectar un resistor de R " . $resistencia . " ohm's a una fuente de V " . $voltaje . " voltios, circulará una corriente de " . $intensidad . " amperios.\n";
?>
