# [RECURSION] PROBLEM LINK: https://codeforces.com/contest/476/problem/B

original = input()
interpreto = input()

# Inicialmente, estoy en la coordenada 0
target = 0

# Paso 1: Hallar cual es la coordenada final a la que debo llegar con mi mensaje interpretado
for instruccion in original:
  target += (1 if instruccion == "+" else -1)
  # if instruccion == "+": target += 1
  # else: target -= 1

# Paso 2: Hallar el total de escenarios en el mensaje que interpreto
# Contar cuantos llegan al target

n = len(original)
wins, fails = 0, 0

# Indice me indica que instrucción de la cadena que yo interpreto debo analizar
# Coordenada me indica en dónde me encuentro actualmente
def recursion(index, coordenada):
  global wins
  global fails

  # Ya no tengo más instrucciones por realizar
  if index == n:
    if coordenada == target:
      wins += 1
    else:
      fails += 1
    return
  
  # La instrucción actual es determinada. NO es una interrogación == NO tengo que elegir
  if interpreto[index] != "?":
    recursion(index + 1, coordenada + (1 if interpreto[index] == "+" else -1))
    return
  
  # Aquí tengo que tomar una decisión:
  # Opcion A: Considero que la ? es un +
  recursion(index + 1, coordenada + 1)

  # Opcion B: Considero que la ? es un -
  recursion(index + 1, coordenada - 1)


recursion(0, 0)
print(f"{wins / (wins + fails):.9f}")
