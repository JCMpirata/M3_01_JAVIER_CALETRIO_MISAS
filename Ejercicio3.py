# Ejercicio 3

from ast import main
import sys
class Producto:

    def __init__(self, nombre, tipo, codigo, precio):
        self.nombre = nombre
        self.tipo = tipo
        self.codigo = codigo
        self.precio = precio

        if self.producto == self.codigo + self.nombre + self.precio + self.tipo:
            print("El producto es correcto")
        else:
            print("No existe ningun producto", file = sys.stderr)

    def __str__(self):
        return "El producto {} del tipo {} y con codigo {} tiene un precio de {} €".format(self.nombre, self.tipo, self.codigo, self.precio)

if "__name__"=="__main__":
    producto1 = Producto("Audi e-tron", "Automovil", 12345, 108500)
    print(producto1)
    producto2 = Producto("Mercedes Eqs", "Automovil", 623548, 112650)
    print(producto2)
    producto3 = Producto("BMW i8", "Automovil", 375458, 104760)
    print(producto3)

    main()