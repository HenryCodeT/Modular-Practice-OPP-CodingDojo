class Producto:
    def __init__(self,producto=0,impuesto=0):
        self.impuesto=impuesto
        self.producto=producto

    def agregar_impuesto(self,amount):
        self.impuesto += amount
        return self.impuesto
