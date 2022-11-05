# Ejercicio 1

from ast import main
import sys
class alumno:
    nombre = input("Introduzca el nombre del alumn@: ")
    nota = float(input("Introduzca la nota del alumn@: "))
    

    def __init__(self):
        if self.alumno == self.nombre + self.nota:
            print("El alumno se ha creado correctamente")
        else:
            print("El alumno no se ha creado corerrectamente", file = sys.stderr)
    
    def calificacion(self):
        for self.resultado in self.nota:
            if self.resultado >= 5:
                print("APROBADO")
            else:
                print("SUSPENDIDO")


if "__name__"=="__main__":
    alumno1 = alumno()
    alumno2 = alumno()
    alumno3 = alumno()
    main()
    


