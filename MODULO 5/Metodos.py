class Robot:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color

    def saludar(self):
        print(f"¡Bip bop! Soy {self.nombre}")

robot1 = Robot("Arturito", "Azul")
robot1.saludar()
