package main

import "fmt"

func main() {
	var nombre string
	fmt.Print("Ingrese su nombre: ")
	fmt.Scan(&nombre)
	var apellido string
	fmt.Print("Ingrese su apellido: ")
	fmt.Scan(&apellido)
	var profesion string
	fmt.Print("Ingrese su profesion: ")
	fmt.Scan(&profesion)
	var nacimiento int
	fmt.Print("Ingrese su año de nacimiento: ")
	fmt.Scan(&nacimiento)
	var edad int
	edad = 2025 - nacimiento
	fmt.Println("Hola", nombre, apellido, "de", edad, "años, eres", profesion)
}
