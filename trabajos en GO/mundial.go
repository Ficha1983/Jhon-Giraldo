package main

import (
	"fmt"
	"strconv"
	"strings"
)

type Equipo struct {
	Nombre string
}

func simularPartido(equipoA, equipoB Equipo) Equipo {
	fmt.Printf("Partido: %s vs %s\n", equipoA.Nombre, equipoB.Nombre)
	fmt.Print("Ingresa el marcador (ej: 2-1): ")
	var marcador string
	fmt.Scanln(&marcador)

	goles := strings.Split(marcador, "-")
	golesA, _ := strconv.Atoi(goles[0])
	golesB, _ := strconv.Atoi(goles[1])

	fmt.Printf("Resultado: %s %d - %d %s\n", equipoA.Nombre, golesA, golesB, equipoB.Nombre)

	if golesA > golesB {
		return equipoA
	}
	return equipoB
}

func simularRonda(equipos []Equipo) []Equipo {
	var ganadores []Equipo
	for i := 0; i < len(equipos); i += 2 {
		if i+1 < len(equipos) {
			ganador := simularPartido(equipos[i], equipos[i+1])
			ganadores = append(ganadores, ganador)
		} else {
			ganadores = append(ganadores, equipos[i]) // Si hay un equipo impar, pasa directo
		}
	}
	return ganadores
}

func main() {
	equipos := []Equipo{
		{Nombre: "Colombia"},
		{Nombre: "Panama"},
		{Nombre: "Mexico"},
		{Nombre: "Argentina"},
		{Nombre: "Peru"},
		{Nombre: "Brasil"},
		{Nombre: "Chile"},
		{Nombre: "Uruguay"},
		{Nombre: "Paraguay"},
		{Nombre: "Ecuador"},
		{Nombre: "Venezuela"},
		{Nombre: "Bolivia"},
		{Nombre: "Costa Rica"},
		{Nombre: "Honduras"},
		{Nombre: "Guatemala"},
		{Nombre: "El Salvador"},
	}

	fmt.Println("¡Comienza el torneo!")

	for len(equipos) > 1 {
		fmt.Println("\n--- Siguiente ronda ---")
		equipos = simularRonda(equipos)
		fmt.Println("Equipos clasificados:", equipos)
	}

	fmt.Printf("\n¡El ganador del torneo es %s!\n", equipos[0].Nombre)
}
