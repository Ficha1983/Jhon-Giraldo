<?php
// Primer bloque de código
$a = true;   // Asignamos el valor booleano 'true' a la variable $a
$b = false;  // Asignamos el valor booleano 'false' a la variable $b
echo ($a && $b) ? 'true' : 'false';  // Usamos '&&' para "and" en PHP y mostramos 'true' o 'false'

// Segundo bloque de código
$a = 2;
$b = 3;
$c = 4;
$d = 10;

echo "\n";  // Para agregar una línea nueva en el resultado

echo (($a == $b) && ($c < $d)) ? 'true' : 'false';  // Comparación y uso de '&&' para "and" en PHP

echo "\n";  // Agregamos una línea nueva

echo (!(($a == $b)) && ($c > $d)) ? 'true' : 'false';  // Usamos '!' para "not" en PHP y '&&' para "and"
?>
