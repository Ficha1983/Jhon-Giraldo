<?php
// Definimos las variables
$a = 10;
$b = 4;

// Multiplicación
echo 'La primera variable es: ' . $a . "\n";
echo 'El signo de la operación es: * \n';
echo 'La segunda variable es: ' . $b . "\n";
$c = $a * $b;
echo 'El resultado es: ' . $c . "\n";
echo 'El tipo de resultado es: ' . gettype($c) . "\n\n";

// División
echo 'La primera variable es: ' . $a . "\n";
echo 'El signo de la operación es: / \n';
echo 'La segunda variable es: ' . $b . "\n";
$c = $a / $b;
echo 'El resultado es: ' . $c . "\n";
echo 'El tipo de resultado es: ' . gettype($c) . "\n\n";

// Suma
echo 'La primera variable es: ' . $a . "\n";
echo 'El signo de la operación es: + \n';
echo 'La segunda variable es: ' . $b . "\n";
$c = $a + $b;
echo 'El resultado es: ' . $c . "\n";
echo 'El tipo de resultado es: ' . gettype($c) . "\n\n";

// Resta
echo 'La primera variable es: ' . $a . "\n";
echo 'El signo de la operación es: - \n';
echo 'La segunda variable es: ' . $b . "\n";
$c = $a - $b;
echo 'El resultado es: ' . $c . "\n";
echo 'El tipo de resultado es: ' . gettype($c) . "\n\n";

// Exponentiation (potencia)
echo 'La primera variable es: ' . $a . "\n";
echo 'El signo de la operación es: ** \n';
echo 'La segunda variable es: ' . $b . "\n";
$c = pow($a, $b);  // En PHP se usa la función pow() para exponentes
echo 'El resultado es: ' . $c . "\n";
echo 'El tipo de resultado es: ' . gettype($c) . "\n\n";

// Módulo (resto de la división)
echo 'La primera variable es: ' . $a . "\n";
echo 'El signo de la operación es: % \n';
echo 'La segunda variable es: ' . $b . "\n";
$c = $a % $b;
echo 'El resultado es: ' . $c . "\n";
echo 'El tipo de resultado es: ' . gettype($c) . "\n";
?>
