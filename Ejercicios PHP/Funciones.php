<?php
// Definimos los arreglos a y b
$a = array(1, 2, 3, 4, 5);
$b = array(6, 7, 8, 9, 10);
$c = array();  // Array vacío para almacenar los resultados

// Iteramos con un bucle for y multiplicamos los elementos correspondientes de los arreglos
for ($contador = 0; $contador < count($a); $contador++) {
    $c[] = $a[$contador] * $b[$contador];  // Multiplicamos y agregamos el resultado al arreglo $c
}

// Imprimimos el arreglo resultante
print_r($c);  // Esta función imprime el contenido del arreglo
?>


<?php
// Función que imprime 'hola'
function mostrar_texto() {
    echo "hola\n";
}

mostrar_texto();  // Llamamos a la función mostrar_texto()

// Función para multiplicar dos números
function multiplicar() {
    $a = 5;
    $b = 8;
    echo $a * $b . "\n";  // Imprimimos el resultado de la multiplicación
}

multiplicar();  // Llamamos a la función multiplicar()

// Función que usa variables globales
function multiplicar() {
    global $a, $b;  // Usamos la palabra clave 'global' para acceder a variables externas
    echo $a * $b . "\n";
}

$a = 5;
$b = 8;
multiplicar();  // Llamamos a la función multiplicar con variables globales

?>


<?php
// Función que retorna el producto de dos números
function multiplicar() {
    $a = 5;
    $b = 8;
    return $a * $b;  // Retornamos el resultado de la multiplicación
}

$Resultado = multiplicar();  // Guardamos el valor retornado
echo $Resultado + 5 . "\n";  // Imprimimos el resultado sumado con 5
?>

<?php
// Función para validar un dato
function validar_dato($a) {
    if ($a == 5) {
        return true;  // Si $a es igual a 5, retornamos true
    } else {
        return false;  // Si no, retornamos false
    }
}

$a = 5;  // Asignamos el valor a la variable $a
$dato = validar_dato($a);  // Llamamos a la función y guardamos el resultado
echo ($dato ? 'True' : 'False') . "\n";  // Imprimimos el resultado
?>


