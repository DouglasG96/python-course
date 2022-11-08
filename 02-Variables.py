#Variables

my_string_variable = "My String Variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = True
print(my_bool_variable)

#Concatenacion de variables en un print
print(my_string_variable,my_int_to_str_variable,my_bool_variable)
print("Este es el valor de:",my_bool_variable)
# Algunas funciones de sistema
print(len(my_string_variable))

#Variables en una sola linea. Cuidado con abusar de esta sintaxis!
name, surname, alias, age = "Douglas", "Guzman", 'DouglasDev', 26
print("Me llamo:", name,". mi edad es:", age, ". mi alias es:", alias, "y mi apellido es:",surname)


# Inputs
"""
first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)
"""

# Cambiamos su tipo
name = 35
age = "Douglas"
print(name)
print(age)

# Forzamos el tipo
address: str = "My Address"
address = 32
address = True
address = 5.2
print(type(address))