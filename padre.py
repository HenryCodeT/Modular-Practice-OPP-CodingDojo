from store import Producto
local_val = "unicornios mágicos"
def square(x):
    return x * x

class Usuario(Producto):
    def __init__(self, name):
        self.name = name
    def di_hola(self):
        return "hola"
if __name__ == "__main__":
    producto = Producto()
    print(producto)
    print(producto.agregar_impuesto(0.18))
else:
    print("El archivo se está ejecutando porque es importado por otro archivo. El archivo se llama:", __name__)