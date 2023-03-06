#En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota. Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
class Alumno:
    def __init__(self, nombre, apellido, curso):
        self.nombre = nombre
        self.apellido = apellido
        self.curso = curso
def mensaje():
    return print("******Bienvenidos******\n ***Ingrese a continuación los datos del alumno***")

a1 = Alumno("Juan", "Perez", 3)
mensaje()
print("Nombre del alumno: ", a1.nombre,"\n", "Apellido: ", a1.apellido,"\n", "curso: ", a1.curso, "\n")

def nota():
    nota= int(input('Ingrese la Nota del Alumno '))
    if nota >= 6:
        print("APROBADO")
    else:
        print("DESAPROBADO")
print('La Nota del Alumno', a1.nombre, 'es:'"\n")
nota()
print("\n")
print("Continuemos con el Siguiente Alumno.")
a2= Alumno("Raul", "Yacanto", 2)
print("nombre del alumno: ", a2.nombre,"\n", "apellido: ", a2.apellido,"\n", "curso: ", a2.curso, "\n")
print('la nota del alumno', a2.nombre, 'es:'"\n")
nota()
print("\n")
print("Hasta luego.")

##da mensaje de none
