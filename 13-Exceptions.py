### Exceptions Handling ###

numberOne = 5
numberTwo = 1
numberTwo = "1"

#try except
try:
    print(numberOne + numberTwo)
    print("No Se ha producido un error")
except:
    print("Se ha producido un error")


#try except else 
try:
    print(numberOne + numberTwo)
    print("No Se ha producido un error")
except:
    #Esto se ejecuta si no se produce una excepcion
    print("Se ha producido un error")
else:
    #Esto se ejecuta si no se produce una excepcion
    print("La ejecucion continúa correctamente")


#try except else finally
try:
    print(numberOne + numberTwo)
    print("No Se ha producido un error")
except:
    #Esto se ejecuta si no se produce una excepcion
    print("Se ha producido un error")
else:
    #Esto se ejecuta si no se produce una excepcion
    print("La ejecucion continúa correctamente")
finally:
    #Se ejecuta siempre
    print("La ejecucion continúa")

#Excepciones por tipo
try:
    print(numberOne + numberTwo)
    print("No Se ha producido un error")
except TypeError:
    #Se ejecuta si se produce una excepcion
    print("Se ha producido un TypeError")
except ValueError:
    #Se ejecuta si se produce una excepcion
    print("Se ha producido un ValueError")

#Captura de la información de la excepcion
try:
    print(numberOne + numberTwo)
    print("No Se ha producido un error")
except ValueError as error:
    print(error)
except Exception as exception:
    print(exception)