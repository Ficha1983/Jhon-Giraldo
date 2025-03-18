<?php
// Solicitamos al usuario que seleccione una figura para calcular su área
echo "Seleccione la figura a calcular su área:\n";
echo "1 para rombo\n";
echo "2 para rectángulo\n";
echo "3 para cuadrado\n";
echo "4 para trapecio\n";
$Figura = trim(fgets(STDIN));  // Leemos la opción del usuario

$Pi = 3.1416;  // Constante Pi
$const = 2;    // Constante para el rombo

// Usamos la estructura switch para manejar las diferentes opciones
switch ($Figura) {
    case '1':  // Caso para el rombo
        echo "Ingresa el valor de la diagonal mayor: ";
        $Dmayor = (int)trim(fgets(STDIN));  // Leemos la diagonal mayor
        echo "Ingresa el valor de la diagonal menor: ";
        $Dmenor = (int)trim(fgets(STDIN));  // Leemos la diagonal menor
        $Area = ($Dmayor * $Dmenor) / $const;  // Fórmula para el área del rombo
        echo "El área del rombo es: " . $Area . "\n";
        break;

    case '2':  // Caso para el rectángulo
        echo "Ingresa el valor del largo del rectángulo: ";
        $Largo = (int)trim(fgets(STDIN));  // Leemos el largo
        echo "Ingresa el valor del ancho del rectángulo: ";
        $Ancho = (int)trim(fgets(STDIN));  // Leemos el ancho
        $Area = $Largo * $Ancho;  // Fórmula para el área del rectángulo
        echo "El área del rectángulo es: " . $Area . "\n";
        break;

    case '3':  // Caso para el cuadrado
        echo "Ingresa el valor del lado del cuadrado: ";
        $Lado = (int)trim(fgets(STDIN));  // Leemos el lado
        $Area = $Lado * $Lado;  // Fórmula para el área del cuadrado
        echo "El área del cuadrado es: " . $Area . "\n";
        break;

    case '4':  // Caso para el trapecio
        echo "Ingresa el valor de la base mayor: ";
        $Bmayor = (int)trim(fgets(STDIN));  // Leemos la base mayor
        echo "Ingresa el valor de la base menor: ";
        $Bmenor = (int)trim(fgets(STDIN));  // Leemos la base menor
        echo "Ingresa la altura del trapecio: ";
        $H = (int)trim(fgets(STDIN));  // Leemos la altura
        $Area = (($Bmayor + $Bmenor) * $H) / 2;  // Fórmula para el área del trapecio
        echo "El área del trapecio es: " . $Area . "\n";
        break;

    default:  // Si el usuario ingresa una opción no válida
        echo "Opción no válida. Por favor, seleccione una figura entre 1 y 4.\n";
        break;
}
?>
