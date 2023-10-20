lives = 5
print(type(lives))
age = 13
buget = 100
temperature = 12.5
print (type(temperature))

lives -= 2 
print(lives)

lives -= 5 
print(lives)
"""
ENERO = 1000
FEBRERO = 30000
MARZO = 40000

Total = ENERO + FEBRERO + MARZO
print("El gasto total es :",Total)

Promedio = Total / 3
print("El pronedio total es :", Promedio)
"""


ENERO = input("Cual es el presupuesto de Enero :")
FEBRERO = input ("Cual es el presupuesto de Febrero :")
MARZO = input ("cual es el presupuesto de Marzo :")

ENERO = int(ENERO)
FEBRERO = int(FEBRERO)
MARZO = int(MARZO)

Total = ENERO + FEBRERO + MARZO
print("El Total de los meses Es:",Total)

Promedio = Total / 3
print("El promedio de los Meses Es",Promedio)

