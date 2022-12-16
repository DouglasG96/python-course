### Loops ###

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else: # Es opcional
    print("Mi condicion es mayor o igual que 10")

print("La ejecucion continua")


while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecucion")
        break

    print(my_condition)
    
print("La ejecucion continua")

# For

my_list = [26,25,62,52,30,30,17]

for element in my_list:
    print(element)

my_tuple = (26, 1.69, "Douglas", "Guzman", "Douglas")

for element in my_tuple:
    print(element)

my_set = {"Douglas","Guzman",26}

for element in my_set:
    print(element)


my_dict = {
    "Nombre": "Douglas", 
    "Apellido": "Guzman", 
    "Edad": 26,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.69
}

for element in my_dict:
    print(element)
    if element == "Edad":
        break
else:
    print("El bucle for para mi diccionario ha finalizado")

print("La ejecucion continua")

for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    else:
        print("Se ejecuta")
else:
    print("El bucle for para mi diccionario ha finalizado")

