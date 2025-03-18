<?php
// Ejercicio 2: Concatenar condiciones con 'if', 'elseif', y 'else'

// Definimos las variables de nombre, edad, país y municipio
$nombre = 'John Giraldo';  // El nombre es 'John Giraldo'
$edad = 15;                // La edad es 15
$pais = 'Colombia';        // El país es 'Colombia'
$municipio = 'Madrid';     // El municipio es 'Madrid'

// Verificamos varias condiciones combinadas usando 'if', 'elseif', y 'else'

// Condición 1: Si el nombre es 'John Giraldo', la edad es 15, el país es 'Colombia' y su municipio es 'Madrid'
if ($nombre == 'John Giraldo' && $edad == 15 && $pais == 'Colombia' && $municipio == 'Madrid') {
    // Si todas las condiciones son verdaderas, se imprime el siguiente mensaje
    echo 'Su nombre es ' . $nombre . ', tiene ' . $edad . ' años, es de ' . $pais . ' y es del municipio ' . $municipio . '<br>';
}

// Condición 2: Si el nombre es 'John Giraldo' pero la edad no es 15
elseif ($nombre == 'John Giraldo' && $edad != 15) {
    // Si esta condición es verdadera, se imprime el siguiente mensaje
    echo 'Su nombre es John Giraldo y no tiene 15 años.<br>';
}

// Condición 3: Si el nombre no es 'John Giraldo' pero la edad es 15
elseif ($nombre != 'John Giraldo' && $edad == 15) {
    // Si esta condición es verdadera, se imprime el siguiente mensaje
    echo 'Su nombre no es John Giraldo y tiene 15 años.<br>';
}

// Si ninguna de las condiciones anteriores es verdadera, se ejecuta esta sección
else {
    // Se imprime este mensaje en caso de que ninguna condición previa se cumpla
    echo 'No se llama John Giraldo ni tiene 15 años.<br>';
}
?>

