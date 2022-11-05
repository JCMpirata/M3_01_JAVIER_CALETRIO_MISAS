# Ejercicio 1

from ast import main
import sys
class alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
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
    alumno1 = alumno("Pablo", 5.6)
    alumno2 = alumno("Daniel", 3.4)
    alumno3 = alumno("Adrian", 6.75)

    print(alumno1)
    print(alumno2)
    print(alumno3)
    main()
    


