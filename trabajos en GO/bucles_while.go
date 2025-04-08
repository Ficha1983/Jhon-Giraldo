package main

import "fmt"

func main() {
	var c int = 0

	for c < 10 {
		fmt.Println(c)
		c++
	}
}

// en GO no existe el bucle while, se utiliza el for
