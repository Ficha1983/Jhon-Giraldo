package main

import "fmt"

func main() {
	var a int
	fmt.Print("Ingresa un número entero: ")
	fmt.Scanln(&a)
	var b int
	fmt.Print("Ingresa otro número entero: ")
	fmt.Scanln(&b)
	fmt.Println("La suma es:", a+b)
	fmt.Println("La resta es:", a-b)
	fmt.Println("La multiplicación es:", a*b)
	fmt.Println("La división es:", a/b)
	fmt.Println("El módulo es:", a%b)
	fmt.Println("La potencia es:", a^b)
	fmt.Println("el numero a es mayor que b:", (a > b))
	fmt.Println("el numero a es menor que b:", (a < b))

}
