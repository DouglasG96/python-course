### Dictionaries ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Douglas", "Apellido": "Guzman", "Edad": 26, 1: "Python"}

my_dict = {
    "Nombre": "Douglas", 
    "Apellido": "Guzman", 
    "Edad": 26,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1: 1.69
}
print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])
print(my_dict[1])

my_dict["Calle"] = "Calle Douglas"
print(my_dict)

del my_dict["Calle"]

print(my_dict)

print("Douglas" in my_dict)
print("Apellido" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["Nombre", 1, "Direccion"]

my_new_dict = dict.fromkeys((my_list))
print((my_new_dict))
my_new_dict = dict.fromkeys(("Nombre", 1, "Direccion"))
print((my_new_dict))
my_new_dict = dict.fromkeys((my_dict))
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict, "Ricardo")
print((my_new_dict))

my_vales = my_new_dict.values()
print(type(my_vales))

print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(list(my_new_dict.values()))
print(tuple(my_new_dict))
print(set(my_new_dict))