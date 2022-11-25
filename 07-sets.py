### Sets ###
my_set =  set()
my_other_set = {}
print(type(my_set))
print(type(my_other_set)) #Inicialmente es un diccionario

my_other_set = {"Douglas","Guzman",26}
print(type(my_other_set))
print(len(my_other_set))

my_other_set.add("DouglasG")
print(my_other_set) #Un set no es una estructura ordenada

my_other_set.add("DouglasG")
print(my_other_set) #Un set no admite repetidos

print ("Douglas" in my_other_set)
print ("Douglis" in my_other_set)

my_other_set.remove("Douglas")
print(my_other_set)

my_other_set.update()
print(len(my_other_set))

del my_other_set
#print(my_other_set) NameError: name 'my_other_set' is not defined


my_set = {"Douglas","Guzman",26}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"JAVA","php",".Netcore"}

my_new_set = my_set.union(my_other_set)
print(my_new_set)
print(my_new_set.union(my_new_set).union(my_set).union({"Javascript","Rails"}))

print(my_new_set.difference(my_set))