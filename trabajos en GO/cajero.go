package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Usuario struct {
	Usuario string
	Clave   string
	Saldo   float64
}

var usuarios = map[string]*Usuario{
	"sebastian": {"sebastian", "1234", 1000.00},
	"esteban":   {"esteban", "1234", 500.00},
}

func main() {
	reader := bufio.NewReader(os.Stdin)

	fmt.Print("Ingrese su usuario: ")
	usuario := readInput(reader)

	fmt.Print("Ingrese su clave: ")
	clave := readInput(reader)

	user, ok := usuarios[usuario]
	if !ok || user.Clave != clave {
		fmt.Println("Usuario o clave incorrectos.")
		return
	}

	fmt.Println("Bienvenido,", user.Usuario)

	for {
		fmt.Println("\nSeleccione una opción:")
		fmt.Println("1. Consultar saldo")
		fmt.Println("2. Retirar dinero")
		fmt.Println("3. Depositar dinero")
		fmt.Println("4. Salir")

		opcion := readInput(reader)

		switch opcion {
		case "1":
			consultarSaldo(user)
		case "2":
			retirarDinero(user, reader)
		case "3":
			depositarDinero(user, reader)
		case "4":
			return
		default:
			fmt.Println("Opción inválida.")
		}
	}
}

func consultarSaldo(usuario *Usuario) {
	fmt.Println("Su saldo es:", usuario.Saldo)
}

func retirarDinero(usuario *Usuario, reader *bufio.Reader) {
	fmt.Print("Ingrese la cantidad a retirar: ")
	cantidad, err := strconv.ParseFloat(readInput(reader), 64)
	if err != nil {
		fmt.Println("Cantidad inválida.")
		return
	}

	if cantidad > usuario.Saldo {
		fmt.Println("Saldo insuficiente.")
		return
	}

	usuario.Saldo -= cantidad
	fmt.Println("Retiro exitoso. Su nuevo saldo es:", usuario.Saldo)
}

func depositarDinero(usuario *Usuario, reader *bufio.Reader) {
	fmt.Print("Ingrese la cantidad a depositar: ")
	cantidad, err := strconv.ParseFloat(readInput(reader), 64)
	if err != nil {
		fmt.Println("Cantidad inválida.")
		return
	}

	usuario.Saldo += cantidad
	fmt.Println("Depósito exitoso. Su nuevo saldo es:", usuario.Saldo)
}

func readInput(reader *bufio.Reader) string {
	input, _ := reader.ReadString('\n')
	return strings.TrimSpace(input)
}
