#Strings#

my_string = "mi string"
my_other_string = 'mi otro string'

print(len(my_string))
print(len(my_other_string))

print(my_string + " "+my_other_string)

my_new_line_string = "este es un string \ncon salto de linea"
print(my_new_line_string)
my_tab_string = "este es un string \tcon salto de linea"
print(my_tab_string)
my_scape_string = "\teste es un string \nescapado"
print(my_scape_string)
my_scape_string = "\\t este es un string \\n escapado"
print(my_scape_string)

#Formateo#

name, surname, age = "douglas", "guzman", 26
print("Mi nombre es: {} {} y mi edad es {}".format(name,surname,age))
print("Mi nombre es: %s %s y mi edad es %d" %(name,surname,age))
print(f"Mi nombre es: {name} {surname} y mi edad es {age}") #Inferencia de datos

#Desempaquetado de caracteres
language = "Python"
a, b, c, d, e, f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

#Division de strings

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

language_slice = language[0:6:2] #Solo posiciones que extrae del string
print(language_slice)

# Reverse Strings

reversed_language = language[::-1]
print(reversed_language)

#Funciones

print(language.capitalize())
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("2".isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.startswith("Py"))