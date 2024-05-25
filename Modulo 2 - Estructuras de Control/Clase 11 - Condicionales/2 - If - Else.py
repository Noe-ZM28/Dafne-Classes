"""
en caso de querer evaluar multiples posibilidades se utiliza elseif


Ejemplo 1

edad = 16
if edad >= 18:
    print("Eres mayor de edad.")
elif edad >= 13:
    print("Eres un adolescente.")

Eres un adolescente.


Ejemplo 2

edad = 19
if edad >= 18:
    print("Eres mayor de edad.")
elif edad >= 13:
    print("Eres un adolescente.")

Eres mayor de edad.

Ejemplo 3

edad = 5
if edad >= 18:
    print("Eres mayor de edad.")
elif edad >= 13:
    print("Eres un adolescente.")



En caso de quere evaluar aquellos casos en los que no se cumple ninguna condición, se usa else, esta misma instrucción se puede utilizar en otras estucturas.

edad = 5
if edad >= 18:
    print("Eres mayor de edad.")
elif edad >= 13:
    print("Eres un adolescente.")
else:
    print("Eres un niño.")

Eres un niño.

"""