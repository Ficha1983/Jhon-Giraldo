<?php
// Definir la lista (en PHP usamos arrays)
$lista = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'viernes', 'sabado'];

// Mostrar el valor en la posición 4 (comenzando desde 0)
echo $lista[4] . "\n";  // Imprime 'viernes'

// Mostrar toda la lista
echo implode(", ", $lista) . "\n";  // Imprime toda la lista: Lunes, Martes, Miercoles, Jueves, viernes, sabado

// Mostrar los elementos desde el índice 0 hasta el índice 2
echo implode(", ", array_slice($lista, 0, 3)) . "\n";  // Imprime: Lunes, Martes, Miercoles

// Definir una lista que contiene varios tipos de datos, incluyendo un array anidado
$lista = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'viernes', 'sabado', 1, 2, 3, ['Esteban', 0.2, 2.25, true]];

// Mostrar los primeros 4 elementos de la lista y los primeros 3 elementos del sub-array en el índice 9
echo implode(", ", array_slice($lista, 0, 4)) . "\n";  // Imprime: Lunes, Martes, Miercoles, Jueves
echo implode(", ", array_slice($lista[9], 0, 3)) . "\n";  // Imprime: Esteban, 0.2, 2.25
?>
