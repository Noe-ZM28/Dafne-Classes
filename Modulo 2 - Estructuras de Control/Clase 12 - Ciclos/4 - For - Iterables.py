"""
Como se menciono en el apartado anterior, for se peude aplicar a iterables, este funciona de forma igual a un foreach en otro lenguaje, cabe resaltar que este no existe en python, pues el for de python mezcla la funcionalidad de un for tradicional y un foreach



Explicación

-   Los iterables son aquellos objetos que como su nombre indica pueden ser iterados, lo que dicho de otra forma es, que puedan ser indexados (listas, tuplas, sets, strings... etc).

-   Los iteradores son objetos que hacen referencia a un elemento, y que tienen un método next que permite hacer referencia al siguiente.


Sintaxis:

for variable in iterable:
    codigo ...


Ejemplo 1

planets = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"]

for planet in planets:
    print(f"{planet} from solar system")

Mercury from solar system
Venus from solar system
Earth from solar system
Mars from solar system
Jupiter from solar system
Saturn from solar system
Uranus from solar system
Neptune from solar system


Ejemplo 2

text = "Dafne"

for character in text:
    print(character)

D
a
f
n
e


Ejemplo 3

personas = [
    {"nombre": "Ana", "edad": 28},
    {"nombre": "Luis", "edad": 34},
    {"nombre": "Maria", "edad": 22},
    {"nombre": "Carlos", "edad": 45}
]

for persona in personas:
    nombre = persona["nombre"]
    edad = persona["edad"]
    print(f"Nombre: {nombre}, Edad: {edad}")


Nombre: Ana, Edad: 28
Nombre: Luis, Edad: 34
Nombre: Maria, Edad: 22
Nombre: Carlos, Edad: 45

"""

