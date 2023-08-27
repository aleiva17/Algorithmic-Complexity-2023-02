# Abrimos el archivo
my_file = open("input.txt")
word_count = 0

# Recorrer cada línea del archivo
for line in my_file:
    word_count += line.count(" ") + 1

print(f"El archivo tiene un total de {word_count} palabras.")

# Cerramos el archivo [IMPORTANTE]
my_file.close()

# Forma más elegante y cierra automáticamente el archivo
with open("input.txt") as file:
    for line in file:
        # Por defecto, line incluye el salto de línea '\n'
        # Con rstrip, podemos quitarlo (sirve para más cosas)
        line = line.rstrip()
        print(line)


data_to_save = [123, "text", 18.40]

with open("output.txt", "w") as file:
    for data in data_to_save:
        # Para escribir en un archivo, obligatoriamente debemos utilizar un string
        # Además, no incluye/agrega el salto de línea por defecto
        file.write(f"{str(data)}\n")
   