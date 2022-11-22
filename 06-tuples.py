### Tuples ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (26, 1.69, "Douglas", "Guzman", "Douglas")
my_other_tuple = (26,30,15)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[-4]) IndexError
# print(my_tuple[-6]) IndexError


print(my_tuple.count("Douglas")) #Cuenta elementos dentro de la tupla con ese valor
print(my_tuple.index("Guzman")) #Imprime el inidice del valor recibido por parametro
print(my_tuple.index("Douglas")) #Imprime el inidice del valor recibido por parametro

#my_tuple[1] = 1.8 'tuple' object does not support item assignment
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "DGuzman"
my_tuple.insert(1, "verde")

my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

#del my_tuple [2]  'tuple' object doesn't support item deletion
del my_tuple
#print(my_tuple) name 'my_tuple' is not defined

# Tupla inmutable
# List mutable