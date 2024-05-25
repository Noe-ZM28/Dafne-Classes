    # TIPOS DE DATOS
"""
Numericos
    - int(20)
        - numero = 0
    - float(20.5)
        - flotante = 0.5
    - complex(1j)
        - complejo = 1j
boleanos
    - bool(True)
        boleano = False

texto
    - str("Hello World")
        - texto = "xd"

mapeo
    - dict(name="John", age=36)
        - {"name":"John", "age":36}

secuencias
    - list(("apple", "banana", "cherry"))
        - ["apple", "banana", "cherry"]

    - tuple(("apple", "banana", "cherry"))
        - ("apple", "banana", "cherry")

    - range(6)

conjuntos
    - set(("apple", "banana", "cherry"))
        - {"apple", "banana", "cherry"}

    - frozenset({"apple", "banana", "cherry"})

Bytes
    - bytes
    - bytearray
"""

# #numeros enteros
# variable_x = int(123)
# variable_y = int("1")
# x = variable_y + variable_x
# print(x)

# flotantes
# flotante_x = float(20)
# flotante_y = 1
# x = flotante_x + flotante_y
# print(x)
# variable_y = float("d fsdfsd") 
# variable_x = float("1.123")

# resultado = variable_y + variable_x 
# print(resultado)

# complejos
# numero_complejo = complex(1j)


#diccionarios
# diccionario = dict(name="Dafne", age=24) -> explicito

# diccionario = {"name":"Dafne", "age":24} -> implicito
# diccionario_2 = diccionario.copy()

# print(diccionario)
# diccionario["name"] = "Noe"
# print(diccionario)
# print(diccionario_2)

#Boleanos
# variable_boleana = bool(1) #False
# print(variable_boleana)


    # - tuple(("apple", "banana", "cherry"))
    #     - ("apple", "banana", "cherry")
#secuencias
    #-Listas
    #ejemplo 1
# lista_y= list(("apple", "banana", "cherry"))
# lista_x = ["apple", "banana", "cherry", 1, True, [1, 2, 1.2]]

# print(lista_x[5][2], lista_x[2])

#     # Ejemplo 2
# lista_y= list(("apple", "banana", "cherry"))
# lista_banana = ["b", "a", "n", "a", "n", "a"]
# lista_x = ["apple", lista_banana, "cherry", 1, True, [1, 2, 1.2]]
# print(lista_x[1])


# lista_y = list(("apple", "banana", "cherry"))
# # lista_x = ["apple", "banana", "cherry", 1, True, [1, 2, 1.2]]
# print(lista_y)
# lista_y[1] = "Dafne"
# print(lista_y)

    # - tuplas
#         # Ejemplo 1
# tupla = tuple(("apple", "banana", "cherry"))
# tuple_x = ("apple", "banana", "cherry")
# tuple_x[1] = "Dafne"
# print(tuple_x)

        # Ejemplo 2
# lista_x = ["apple","apple","apple","apple","apple",  "banana", "cherry", 1, True, [1, 2, 1.2]]
# print(lista_x)
# tupla = tuple(lista_x)
# tupla[1] = "Dafne"
# print(tupla)

    # - sets
# #         # Ejemplo 1
# lista_x = ["apple","apple","apple","apple","apple", "banana", "cherry"]
# set_x = set(lista_x)
# print(set_x)

# #         # Ejemplo 2
# lista_x = ["apple","apple","apple","apple","apple", "banana", "cherry"]
# set_x = set(lista_x)
# print(set_x)
# set_x[0] = "Dafne"
# print(set_x)

    # - frozenset
# #         # Ejemplo 1

# frozen_set = frozenset({"apple", "banana", "cherry"})
# frozen_set[1] = ""
