from personaje import personaje

class Guerrero (personaje):
    def __init__(self, nombre, salud):
         super(). __init__(nombre, salud)
         self.arma = None

    def equipar_arma(self, arma):
        self.arma =arma
        print(f"{self.nombre} ha equipado el arma: {arma.nombre}")

    def atacar(self, objetivo):
        if self.arma:
            print(f"{self.nombre} ataca con { self.arma.nombre}")
            objetivo.recibir_danio(self.arma.danio)
        else:
            print(f"{self.nombre} no tienun arma equipada")
