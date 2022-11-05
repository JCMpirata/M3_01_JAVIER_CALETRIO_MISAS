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
            if self.nota >= 5:
                return True
            else:
                return False


if "__name__"=="__main__":
    alumno1 = alumno("Pablo", 5.6)
    print(alumno1)
    alumno2 = alumno("Daniel", 3.4)
    print(alumno2)
    alumno3 = alumno("Adrian", 6.75)
    print(alumno3)

    calificacion = alumno.calificacion
    if calificacion >= 5:
        print("APROBADO")
    else:
        print("SUSUPENSO")

    main()
    


