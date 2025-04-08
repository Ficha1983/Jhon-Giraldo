package main

import "fmt"

func main() {
	nombres := []string{"Ana", "Juan", "María", "Pedro"}

	// Mostrar la lista completa
	fmt.Println("Lista de nombres:", nombres)

	// Mostrar elementos individuales usando un bucle for
	fmt.Println("Nombres individuales:")
	for i, nombre := range nombres {
		fmt.Printf("Índice: %d, Nombre: %s\n", i, nombre)
	}
}
