package main

import (
	"fmt"
	"math"
)

func main() {

	fmt.Print("Ingresa la figura que deseas calcular: ")
	fmt.Print("1. Cuadrado\n")
	fmt.Print("2. Rectángulo\n")
	fmt.Print("3. Triángulo\n")
	fmt.Print("4. Círculo\n")
	fmt.Print("5. Salir\n")
	var num1 int
	fmt.Scanln(&num1)

	switch num1 {
	case 1:
		{
			var lado float64
			fmt.Print("Ingresa el lado del cuadrado: ")
			fmt.Scanln(&lado)
			fmt.Println("El área del cuadrado es:", lado*lado)
		}
	case 2:
		{
			var base float64
			fmt.Print("Ingresa la base del rectángulo: ")
			fmt.Scanln(&base)
			var altura float64
			fmt.Print("Ingresa la altura del rectángulo: ")
			fmt.Scanln(&altura)
			fmt.Println("El área del rectángulo es:", base*altura)
		}
	case 3:
		{
			var base float64
			fmt.Print("Ingresa la base del triángulo: ")
			fmt.Scanln(&base)
			var altura float64
			fmt.Print("Ingresa la altura del triángulo: ")
			fmt.Scanln(&altura)
			fmt.Println("El área del triángulo es:", (base*altura)/2)
		}
	case 4:
		{
			var radio float64
			fmt.Print("Ingresa el radio del círculo: ")
			fmt.Scanln(&radio)
			fmt.Println("El área del círculo es:", math.Pi*math.Pow(radio, 2))
		}
	case 5:
		{
			fmt.Println("Saliendo del programa...")
		}
	}
}
