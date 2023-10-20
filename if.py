

## USO DE IF Y ELIF
pet = input('Cual es tu Mascota Favorita? ')

if pet == 'perro':
   print('Genial tienes buen gusto')
elif pet == 'gato':
  print('espero tengas buenas suerte')
elif pet == 'loro':
  print('fantasitico son muy lindos')
else:
 print("no tienes buen gusto en lo absoluto.")


## uso de if con operadores aritmeticos 

stock = int(input('Digita el stock => '))
if stock >= 100 and stock <= 1000:
  print('el stock es correcto')
else:
  print('el stock es incorrecto')

##NUMERO PAR E IMPAR 

number = int(input("ingresa un numero => "))
result = number % 2
if (result == 0):
  print(f'Felicitaciones el {number} es PAR')
else:
  print(f'El {number} NO ES PAR ')












  



