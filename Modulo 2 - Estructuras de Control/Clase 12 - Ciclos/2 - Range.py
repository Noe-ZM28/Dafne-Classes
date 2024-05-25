#range()
"""
Para iterar una N cantidad de veces, se utiliza Range(), esta retorna una secuencia de numeros.
Existen 2 formas de usar la función range, las cuales son:

- range(stop)
    Esta permite obtener una secuencia inmutable de numeros comenzando desde 0, hasta 1 menos que el valor indicado, siendo este la longitud de la secuencia (stop).

    Ejemplos

    1)  list(range(5))
        - [0, 1, 2, 3, 4]

    2)  list(range(8))
        - [0, 1, 2, 3, 4, 5, 6, 7]

    3)  list(range(2))
        - [0, 1]

- range(start, stop[, step])
    Esta permite obtener una secuencia inmutable de rangos de numeros.

    start
        - El valor del parámetro start (0 si no se utiliza el parámetro)
    stop
        - El valor del parámetro stop
    step
        - El valor del parámetro step (1 si no se utiliza el parámetro)

    Ejemplos
    
    1)  list(range(10))
        - [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        
    2)  list(range(1, 11))
        - [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        
    3)  list(range(0, 30, 5))
        - [0, 5, 10, 15, 20, 25]
        
    4)  list(range(0, 10, 3))
        - [0, 3, 6, 9]
        
    5)  list(range(0, -10, -1))
        - [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
        
    6)  list(range(0))
        - []
        
    7)  list(range(1, 0))
        - []

"""


