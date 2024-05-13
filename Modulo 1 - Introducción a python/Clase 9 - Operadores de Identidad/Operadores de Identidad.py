"""
Un operador de identidad se emplea para comprobar si dos variables emplean la misma ubicación en memoria.

is y is not son operadores de identidad.

is devuelve True si los operandos se refieren al mismo objeto. En caso contrario devuelve False.

is not devuelve True si los operandos no se refieren al mismo objeto. En caso contrario devuelve False.

Ten en cuenta que dos valores, cuando son iguales, no implica necesariamente que sean idénticos.
"""


"""
a = 3
b = 3  
c = 4
print a is b # muestra True
print a is not b # muestra False
print a is not c # muestra True

x = 1
y = x
z = y
print z is 1 # muestra True
print z is x # muestra True

str1 = "XXX"
str2 = "XXX"

print str1 is str2 # muestra True
print "Code" is str2 # muestra False

a = [10,20,30]
b = [10,20,30]

print a is b # muestra False (ya que las listas son objetos mutables en Python)
"""

