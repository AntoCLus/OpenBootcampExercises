import _thread
import time
def horaActual(nombre_thread, tiempo_de_espera):
    count = 0
    while count <5:
        time.sleep(tiempo_de_espera)
        count +=1
        print(f'hilo: {nombre_thread}- {time.ctime(time.time())}')

_thread.start_new_thread(horaActual("thread_uno", 1))
_thread.start_new_thread(horaActual("thread_dos", 2))
print('he disparado los hilos')

###############################################3
import logging
logging.info('arrancando programa')
logging.warning('hace calor')
logging.basicConfig(level=logging.INFO)
logging.error('test')
logging.critical('adios')
##################################################
#map   #filter          #reduce
#filter extrae el resultado cuando se cumple el true
numeros = [1, 2, 4, 6, 8, 18]
def mifuncion(x):
    if x% 2 ==0:
        return True
    return False
resultado = filter(mifuncion, numeros)
resultado = filter(lambda x: x%2 == 0, numeros)
print(list(resultado))

def mifuncion2(y):
    if str(y).startswith('pep'):
        return True
    return False
resultado2 = filter(lambda y: srt(y).startwith('pep'), ["pepe", "pepito, "juan"])
print(list(resultado2))

#map ejecuta toda la lista
def cuadrado(x):
    return x *x
resultado3 = map(cuadrado, [1, 2, 3, 4, 5, 6, 7, 8, 9])
resultado3 = map(lambda x: x * x,[1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(resultado3))

#reduce
from functools import reduce
def suma(x, y):
    return x + y
res = reduce(suma, [,2 ,3,4, 5])
print(res)4

#tuple elemento inmutable
cursos = ['Java', 'python', 'git']
asistentes [15, 20, 4]
demo = zip(cursos, asistentes)
#me asocia los elementos de la primera lista con el de la segunda
#java 15, 

#palabras reservadas allse tienen que cumplir todas las condiciones any se puede cumplir una
listaA= [1 ==2, 2==2, 3==4]
res2 = any(listaA)
print (res2)

#ordenar listas
lista = ['pais', 'country']
ordenada = sorted(lista)
#otra forma es
ordenada = sorted(lista, reverse=True, key=lambda x: str(x).startwith('a'))
print(ordenada)


