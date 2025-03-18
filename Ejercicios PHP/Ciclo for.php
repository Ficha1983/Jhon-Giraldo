<?php
// Solicitar el primer valor
echo "Ingrese el primer valor: ";
$A = (int) fgets(STDIN);

// Inicializar B (aunque no se usa en el código de Python)
$B = 0;

// Solicitar el segundo valor
echo "Ingrese el segundo valor: ";
$C = (int) fgets(STDIN);

// Calcular la potencia
$valor = pow($A, $C);  // Calcula A elevado a C

// Imprimir el resultado
echo "La potencia de $A sobre $C es: $valor\n";
?>
