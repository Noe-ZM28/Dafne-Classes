# Salida de datos

print()

# Cadena formateada (f-string)

año = 2016
evento = 'venta'
print(f'Resultados de la {evento} de {año}')
# Salida: Resultados de la venta de 2016


# Método format()

print('Somos los {} que dicen "{}!"'.format('caballeros', 'Ni'))
# Salida: Somos los caballeros que dicen "Ni!"

print('{0} y {1}'.format('jamón', 'huevos'))
# Salida: jamón y huevos

print('{1} y {0}'.format('jamón', 'huevos'))
# Salida: huevos y jamón

print('Este {comida} está {adjetivo}.'.format(
      comida='jamón', adjetivo='absolutamente horrible'))
# Salida: Este jamón está absolutamente horrible.

print('La historia de {0}, {1}, y {otro}.'.format('Juan', 'Manuel',
                                                   otro='Luis'))
# Salida: La historia de Juan, Manuel, y Luis.
