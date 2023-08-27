# Existen dos formas de inicializar una lista
data_a = []
data_b = list()

# Para acceder a la lista de métodos, basta con colocar .
# para que el editor o IDE nos ayude
data_a.append(2) # Agregar al final
data_a.insert(0, 99) # Inserta elemento antes del index (0: index, 2: elemento)
print(data_a.count(2)) # Imprime cuántas veces se encuentra el 2

# Ordenar la lista ascendentemente
data_a.sort()
print(data_a) # Imprime la lista en el formato: [elemento_1, elemento_2, ..., elemento_n]

# Ordenar la lista descendentemente
data_a.sort(reverse=True)

# Iteración sobre cada elemento del arreglo
for value in data_a:
    # Imprimir cada valor sin que coloque el salto de línea (por defecto) al final
    print(value, end=" -> ")

# Imprimir salto de línea
print()

# Recorre en reversa la lista: O(1)
for value in reversed(data_a):
    print(value, end=", ")
