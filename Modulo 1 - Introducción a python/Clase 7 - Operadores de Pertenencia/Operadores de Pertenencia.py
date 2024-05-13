"""
Un operador de pertenencia se emplea para identificar pertenencia en alguna secuencia (listas, strings, tuplas).

in y not in son operadores de pertenencia.

in devuelve True si el valor especificado se encuentra en la secuencia. En caso contrario devuelve False.

not in devuelve True si el valor especificado no se encuentra en la secuencia. En caso contrario devuelve False.

"""

"""
a = [1,2,3,4,5]
  
#Esta 3 en la lista a?
print 3 in a # Muestra True 
  
#No está 12 en la lista a?
print 12 not in a # Muestra True
  
str = "Hello World"
  
#Contiene World el string str?
print "World" in str # Muestra True
  
#Contiene world el string str? (nota: distingue mayúsculas y minúsculas)
print "world" in str # Muestra False  

print "code" not in str # Muestra True
"""