<?php
// Solicitar al usuario que ingrese sus datos
echo "Escriba sus nombres completos: ";
$a = trim(fgets(STDIN));  // Leemos el nombre completo
echo "Escriba sus apellidos completos: ";
$b = trim(fgets(STDIN));  // Leemos los apellidos completos
echo "Escriba su profesion: ";
$c = trim(fgets(STDIN));  // Leemos la profesión
echo "Escriba su año de nacimiento: ";
$d = (int)trim(fgets(STDIN));  // Leemos el año de nacimiento y lo convertimos a entero

// Calculamos la edad
$e = 2025 - $d;

// Imprimir la información completa
echo "El (La) " . $c . " " . $a . " " . $b . " tiene " . $e . " años.\n";
?>
