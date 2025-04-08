package main

import "fmt"

func main() {
	var v, r, i float64
	fmt.Print("Ingrese el valor de la tension (v): ")
	fmt.Scan(&v)
	fmt.Print("Ingrese el valor de la resistencia (r): ")
	fmt.Scan(&r)
	i = v / r
	fmt.Println("al conectar una resistencia de", r, "Ohm con una tension de", v, "V, la intensidad de la corriente es de", i)
}
