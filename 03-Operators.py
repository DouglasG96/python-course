#Operadores aritmeticos#
print(3+4)
print(3-4)
print(3*4)
print(3/4)
print(10 % 3)
print(10 // 3) #aproxima a un numero entero la division
print(2 ** 3) #calcular un exponente
print(2 ** 3 + 3 - 7 / 1 // 2)

print("hola " + "python "+ "Que tal?") #Concatenacion
print("hola " + str(5))
print("hola " * 5)
print("hola " * (5*3))
my_float = 2.5 * 2
print("hola " * int(my_float))

#Operadores comparativos #

print(3 > 4)
print(3 < 4)
print(3 <= 4)
print(3 >= 4)
print(3 == 4)
print(3 != 4)

print("Hola" > "Python")
print("Hola" < "Python")
print("aaaa" < "abaa") #Valida la ordenacion alfabetica por ASCII
print(len("aaaa") < len("abaa")) #Cuenta caracteres
print("Hola" <= "Python")
print("Hola" >= "Python")
print("Hola" == "Python")
print("Hola" != "Python")

#Operadores logicos#

print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 1))
print(not(3 > 4))