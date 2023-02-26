message = "Bienvenidos a invierte el orden"
print(message)
numero1 = int(input('ingrese un número   '))
numero2 = int(input('ingrese un número   '))
numero3 = int(input('ingrese un número   '))
list1 = [numero1, numero2, numero3]
list1.reverse()
print(list1)


print('**********************')
list2 = list(range(1, 100))
list2.reverse()
print(list2)