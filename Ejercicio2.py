from ast import main
import sys

class alumno:

    nombre = input("Introduzca el nombre del alumno: ")
    nota = float("Introduzca la nota del alumno: ")
    
    def __init__(self):
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
    alumno1 = alumno()
    alumno2 = alumno()
    alumno3 = alumno()
    main()
    