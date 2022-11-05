# Ejercicio 3

from ast import main
import sys
class Producto:
    codigo = int("Introduzca el codigo del producto: ")
    nombre = input("Introduzca el producto: ")
    precio = float("Introduzca el precio: ")
    tipo = input("Introduzca el tipo: ")

    def __init__(self):
        if self.producto == self.codigo + self.nombre + self.precio + self.tipo:
            print("El producto es correcto")
        else:
            print("No existe ningun producto", file = sys.stderr)

    def __str__(self):
        cadena = "El producto " + self.nombre + "del tipo " + self.tipo + "y con el codigo " + self.codigo + "cuesta " + self.precio + "€"
        return cadena

if "__name__"=="__main__":
    producto1 = Producto()
    producto1.__init()
    producto1.__str__()

    main()