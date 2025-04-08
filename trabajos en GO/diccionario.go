package main

import "fmt"

func main() {

	var diccionario = map[string]string{
		"marca":  "ford",
		"color":  "rojo",
		"modelo": "sedan",
		"placa":  "ROS227",
	}

	fmt.Println(diccionario["color"])
	diccionario["color"] = "verde"
	fmt.Println(diccionario["color"])
	fmt.Print(diccionario["marca"])
	diccionario["marca"] = "chevrolet"
	fmt.Println(diccionario["marca"])

	fmt.Println(diccionario)

}
