package main

import "fmt"

func main() {
	var a = 10
	fmt.Println("Ingresa un número: ")
	fmt.Scanln(&a)
	if a > 2 {
		fmt.Println("El número es mayor que 2")
	} else {
		fmt.Println("El número es menor o igual a 2")
	}

	var n = "sebastian"
	var e = 22
	var p = "colombia"

	if n == "sebastian" && e == 22 && p == "colombia" {
		fmt.Println("El nombre es sebastian, la edad es 22 y el país es colombia")
	} else if n == "sebastian" && e == 22 && p == "colombia" {
		fmt.Println("No coincide con los datos")
	}
	else {

	}
	}
	}

}
