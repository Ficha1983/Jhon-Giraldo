<?php
// Solicitar al usuario que ingrese los valores de A y B
echo "Ingrese el valor para A: ";
$A = (int)trim(fgets(STDIN));  // Leer el valor de A y convertirlo a entero

echo "Ingrese el valor para B: ";
$B = (int)trim(fgets(STDIN));  // Leer el valor de B y convertirlo a entero

// Realizar las operaciones
$suma = $A + $B;
echo "La suma de los números es: " . $suma . "\n";

$res = $A - $B;
echo "La resta de los números es: " . $res . "\n";

$multi = $A * $B;
echo "La multiplicación de los números es: " . $multi . "\n";

$div = $A / $B;
echo "La división de los números es: " . $div . "\n";

// Comparaciones
$igual = ($A == $B);
echo "El número es igual: " . ($igual ? "Sí" : "No") . "\n";

$mayor = ($A > $B);
echo "El número menor es: " . ($mayor ? $B : $A) . "\n";
echo "El número mayor es: " . ($mayor ? $A : $B) . "\n";
?>
