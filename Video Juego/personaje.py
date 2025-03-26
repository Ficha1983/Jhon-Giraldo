class personaje:
    def __init__(self, nombre, salud):
        self.nombre = nombre
        self.salud = salud
    def recibir_danio(self, cantidad):
        self.salud -= cantidad
        print(f"{self.nombre} ha recibido {cantidad} dedaño. Salud restante: {self.salud}")
