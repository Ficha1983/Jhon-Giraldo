package main

import (
	"fmt"
	"math"
)

func main() {
	num1 := 10
	num2 := 5
	suma := num1 + num2
	resta := num1 - num2
	multiplicacion := num1 * num2
	division := num1 / num2
	modulo := num1 % num2
	potencia := math.Pow(float64(num1), float64(num2))

	fmt.Println("La suma es:", suma)
	fmt.Println("La resta es:", resta)
	fmt.Println("La multiplicación es:", multiplicacion)
	fmt.Println("La división es:", division)
	fmt.Println("El módulo es:", modulo)
	fmt.Println("La potencia es:", potencia)
}
