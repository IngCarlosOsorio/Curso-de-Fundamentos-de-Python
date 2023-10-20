
#while True:
#  print('se ejecuto')
'''
counter = 0 
while counter < 10:
  counter += 1 
  print(counter)


counter = 0 
while counter < 20:
  counter += 1 
  if counter == 15:
    break
  print(counter)
    '''

counter = 0
while counter < 10:
    counter +=1
    if counter ==5:
        break # Rompe un flujo o ciclo de manera forzada
    print(counter)

#
counter1 = 0
while counter1 < 20:
    counter1 +=1
    if counter1 < 15:
        continue #El bucle no termina sino que continúa con la siguiente iteración.
print(counter1)
