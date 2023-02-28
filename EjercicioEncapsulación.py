#Crear clase Persona.
#Crear variables las privadas edad, nombre y telefono de la clase Persona.
class Persona:
    def __init__(self, nombre, edad, telefono):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono

    #Crear gets y sets de cada propiedad.
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value
    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, value):
         self._edad = value

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, value):
        self._telefono = value

#Crear un objeto persona en el main.
p1 = Persona ("Ana", 54, 36578)
print("su nombre es", p1.nombre)
print("su edad es", p1.edad)
print("su tel es", p1.telefono)

#Utiliza los gets y sets para darle valores a las propiedades edad, nombre y telefono, por último muéstralas por consola.
p2 = Persona(input('nombre '), input('edad  '), input('telefono '))

from EjercicioEncapsulación import Persona
p3 = Persona('Juan', 23, 145)






