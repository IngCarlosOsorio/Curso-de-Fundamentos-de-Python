name = "carlos"
last_name = "osorio"
my_age = "32"
print(name)
print(last_name)


full_name = name +" "+ last_name
print('El nombre completo es : =>', full_name)

quote = "I am carlo's"
print(quote)

quote2 = ' She is very tall "Hello jaja" '
print(quote2)

#formato

template = "Hola my name is " + name + " y mi apellidos es " + last_name
print('v1',template)


template = "Hola, Mi nombres es {} y mi apellido es {}".format(last_name,name)
print('v2',template)


template = f"Hola, Mi nombres es {name} y mi apellido es {last_name}"
print('v3',template)

#nombre , apellido , edad 


template = f"Hola, Mi nombres es {name} y mi apellido es {last_name} tengo {my_age} años"
print('v4',template)


