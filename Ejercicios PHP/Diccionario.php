<?php
// Creación de un array asociativo (equivalente a un diccionario en Python)
$coche = array(
    'marca' => 'Ford',
    'color' => 'rojo',
    'modelo' => 'sedan',
    'placa' => 'ROS227'
);

// Imprimir el color
echo $coche['color'] . "\n";

// Cambiar el valor del color
$coche['color'] = 'verde';
echo $coche['color'] . "\n";

// Imprimir la marca
echo $coche['marca'] . "\n";

// Cambiar el valor de la marca
$coche['marca'] = 'Renault';
echo $coche['marca'] . "\n";

// Imprimir el array completo
print_r($coche);
?>
