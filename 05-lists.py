# Lists #

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [26,25,62,52,30,30,17]

print(my_list)

print(len(my_list))

my_other_list = [26, 1.69, "douglas", "guzman"]

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_other_list[-4])
print(my_other_list.count('guzman'))
print(my_list.count(30))
#print(my_other_list[4]) IndexError
#print(my_other_list[-5]) IndexError

#Desrtructuracion de una lista, se necesitan todos los elementos
age, height, name, surname = my_other_list
print(name) #imprime los valores de esa posicion del elemento

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)

print(my_list + my_other_list)
#print(my_list * my_other_list)

my_other_list.append("DouglasDev") #Agrega a la ultima posicion de la lista
print(my_other_list)

my_other_list.insert(1,"Rojo") #Agrega en la posicion indicada de la lista
print(my_other_list)

my_other_list[1] = "Verde"
print(my_other_list) 

my_other_list.remove("Verde") #Elimina el valor recibido por parametro
print(my_other_list)

my_list.remove(30) #Elimina el valor recibido por parametro
print(my_list)

print(my_list.pop()) #Elimina ultimo elemento de la lista
print(my_list)

print(my_list.pop(2)) #Elimina el valor que recibe por parametro
print(my_list)

my_pop_element = my_list.pop(2) #Retorna el valor eliminado (no el indice)
print(my_pop_element)
print(my_list)

del my_list[2] #Elimina sin retornar el valor eliminado (como con pop)
print(my_list)

my_new_list = my_list.copy() # Copia toda la lista 
my_list.clear() #Elimina la lista completa
print(my_list)
print(my_new_list)
my_new_list.reverse() #Voltea de posicion todos los valores de la lista
print(my_new_list)

my_new_list.sort() #Ordena de mayor a menor la lista u orden alfabetico
print(my_new_list)

my_list = "hola Python"

print(my_list)
print(type(my_list))