# Ejercicio 2

from ast import main
import sys

class alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        if self.alumno == self.nombre + self.nota:
            print("El alumno se ha creado correctamente")
        else:
            print("El alumno no se ha creado correctamente", file = sys.stderr)
        

    def calificacion(self):
        for self.resultado in self.nota:
            if self.resultado >= 5:
                print("APROBADO")
            else:
                ("SUSPENDIDO")

    def __str__(self):
        cadena = "El alumno" + self.alumno + "ha sacado" + self.nota + "por lo que ha " + calificacion()
        return cadena


if "__name__"=="__main__":
    alumno1 = alumno("Pablo", 6.5)
    alumno2 = alumno("Daniel", 3.4)
    alumno3 = alumno("Adrian", 7,75)
    main()
    