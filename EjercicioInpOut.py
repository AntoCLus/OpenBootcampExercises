f = open('holis.txt', 'r+')
print(f.readline())
agregar = f.write('tara es hermosa también')
print(agregar)
f.close()