
# Todos los inputs se capturan como strings y la línea completa escrita
line = input("Este mensaje puede ser opcional: ")
print(line)

# Si queremos dividir el input (la línea entera) podemos usar split.
# Esto hará que inputs sea una list de strings. Por defecto, divide
# el string por los espacios vacíos.
inputs = input().split()
print(inputs)

# Podemos también dividir el input (string) por un caracter con el parámetro opcional
text = "a0b0c0d"
letters = text.split("0")
print(letters)