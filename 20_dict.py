person = {
  'name' : 'carlos',
  'last_name' : 'osorio',
  'langs' : ['python', 'javascript'],
  'age' : 100
}

print(person)

person['name'] = 'Carlos'
person['age'] -= 50
person['langs'].append('rust')
print(person)


del person['last_name']
person.pop('age') #eliminar
print('keys')
print(person.keys())

print('values')
print(person.values())
