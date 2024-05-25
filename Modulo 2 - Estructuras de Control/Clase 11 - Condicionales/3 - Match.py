"""
La estructura Match solo funciona apartir de python 3.10

Si bien en python no exixte swith para evaluar los multiples valores que puede tener una variable, este cuenta con match, el cual permite una funcionalidad similar, ademas de permitir usar condiciones logicas dentro.

sintaxis:

match variable:
    case patron1:
        # Bloque de código para patrón1
    case patron2:
        # Bloque de código para patrón2
    case _:
        # Bloque de código por defecto si no hay coincidencia

El patrón _ actúa como un comodín que coincide con cualquier valor si no se ha encontrado ninguna coincidencia anterior, similar al default en un switch.

Ejemplo 1

comando = "iniciar"

match comando:
    case "iniciar":
        print("El sistema se está iniciando.")
    case "detener":
        print("El sistema se está deteniendo.")
    case _:
        print("Comando no reconocido.")

El sistema se está iniciando.


Ejemplo 2
Mathch funciona con diferestes tipos de datos

persona = {"nombre": "Ana", "edad": 28}

match persona:
    case {"nombre": nombre, "edad": edad}:
        print(f"Nombre: {nombre}, Edad: {edad}")
    case _:
        print("Formato de persona no reconocido.")

Nombre: Ana, Edad: 28


Ejemplo 3

Se pueden guardar partes de un patrón utilizando as para hacer referencias más fáciles.

punto = (3, 4)

match punto:
    case (x, y) if x == y:
        print(f"El punto está en la línea x = y en ({x}, {y}).")
    case (x, y) as pt:
        print(f"El punto está en {pt}.")

El punto está en (3, 4)



Ejemplo 4
Se pueden aueden añadir condiciones adicionales a los patrones utilizando if.

punto = (3, 4)

match punto:
    case (x, y) if x == y:
        print(f"El punto está en la línea x = y en ({x}, {y}).")
    case (x, y) if x < y:
        print(f"El punto está por debajo de la línea x = y en ({x}, {y}).")
    case (x, y):
        print(f"El punto está en ({x}, {y}).")

El punto está por debajo de la línea x = y en (3, 4).

"""
