
"""
While
Es una estructura de control que se ejecuta una cantidad indeterminada de veces siempre y cuando se cumpla una condición logica.

Sintaxis:

    while condition:
        code ...

Ejemplo:
    numero = 0
    while number < 10:
        print(f"El numero es: {numero}")
        numero += 1

El numero es: 0
El numero es: 1
El numero es: 2
El numero es: 3
El numero es: 4
El numero es: 5
El numero es: 6
El numero es: 7
El numero es: 8
El numero es: 9



En caso de querer modificar el flujo de los ciclos, existe continue, que permite saltar a ls siguiente irteración y break, que detiene la ejecución del ciclo, estas 2 palabras recervadas funcionan tambien dentro de for.

continue
    Ejemplo:
        numero = 0
        while numero < 10:
            if numero == 1:
                numero += 1
                continue
            else:
                print(f"El numero es: {numero}")
            numero += 1

            El numero es: 0
            El numero es: 2
            El numero es: 3
            El numero es: 4
            El numero es: 5
            El numero es: 6
            El numero es: 7
            El numero es: 8
            El numero es: 9
        
break
    Ejemplo:
        numero = 0
        while numero < 10:
            if numero == 1:
                numero += 1
                break
            else:
                print(f"El numero es: {numero}")
            numero += 1

    El numero es: 0
"""


#Nota: No existe Do While, sin embargo se peude emular su comportamiento

