from functools import reduce
numeros = [1, 2, 4, 5, 6, 9, 18]
def mifuncion(x):
    if x% 2 == 0:
        return True
    return False

resultado = filter(mifuncion, numeros)
print(list(resultado))

def suma (resultado, y):
    return resultado + y

res = reduce(suma, [2, 4, 6, 18])
print(res)