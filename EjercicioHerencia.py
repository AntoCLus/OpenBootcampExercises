from EjercicioEncapsulación import Persona
#Crea una clase Persona con las siguientes variables:nombre, edad, tel
#na vez creada la clase, crea una nueva clase Cliente que herede de Persona, esta nueva clase tendrá la variable credito solo para esa clase.
class Cliente(Persona):
    def __init__(self,nombre, edad, telefono, credito):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.credito = credito
#Crea ahora un objeto de la clase Cliente que debe tener como propiedades la edad, el telefono, el nombre y el credito, tienes que darles valor y mostrarlas por pantalla.
cliente1 = Cliente('Alberto', 23, 1549876, 3000)
print("El nombre del cliente es: ", cliente1.nombre)
print(cliente1.nombre, "cuenta con el siguiente crédito : ", cliente1.credito, 'dólares')
print(cliente1.nombre, 'corrobore su nro de tel: ', cliente1.telefono)
#aqui podemos agregarle:
#t == input("si su telefono es correcto escriba (si/no)")
#if t == "no":
#    print("escriba su tel correctamente ")
#    cliente1.telefono = input(" ")
#else: t == "si"
#print("excelente")
#break
            


#Una vez hecho esto, haz lo mismo con la clase Trabajador que herede de Persona, y con una variable salario que solo tenga la clase Trabajador.
class Trabajador(Cliente):
     def __init__(self,nombre, edad, telefono, credito, salario):
       super().__init__(nombre, edad, telefono, credito)
       self.salario = salario
trabajador1 = Trabajador('Antonio', 52, 61978, 3000, 25000)
print("el salario de ", trabajador1.nombre, "es ", trabajador1.salario)