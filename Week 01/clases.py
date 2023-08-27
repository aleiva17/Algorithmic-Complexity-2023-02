from random import randint

class MyClass:
    # Constructor
    def __init__(self) -> None:
        # Atributos
        self.attribute_a = randint(1, 20)
        self.attribute_b = randint(1, 20)
        self.attribute_c = randint(1, 20)
        self.__private_attribute = []
    
    def method_a(self):
        print("Método sin parámetros")
    
    def method_b(self, foo):
        print(f"Método con parámetro: {foo}")

    # Permite hacer print(obj), donde obj es un objeto de la clase
    def __str__(self) -> str:
        return f"{self.attribute_a} - {self.attribute_b} - {self.attribute_c}"
    


obj = MyClass()
obj.method_a()
obj.method_b(obj)

print(obj)

# No hace falta utilizar/llamar al destructor
# El mismo garbage collector de python se encarga