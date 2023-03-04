#En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
#color ruedas puertas

class Vehicle:
    def __init__(self, color, wheels, doors):
        self.color = color
        self.wheels = wheels
        self.doors = doors

class Car(Vehicle):
    def __init__(self, speed, type):
        self.speed = 120
        self.type = "ford"
        Vehicle.__init__(self, "green", 4, 4)
        #Vehicle.__init__(self, color=input('set the color: '), wheels=input('how many wheels: '), doors=input('how many wheels: '))

c1 = Car(120, "Ford")
print(c1.color)
print(c1.wheels)
print(c1.doors, c1.type, c1.speed)
c2 = Car(150, "Citroen")
print(c2.color, c2.type)
c1.doors

