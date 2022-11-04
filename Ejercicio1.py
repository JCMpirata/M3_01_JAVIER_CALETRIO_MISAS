from ast import main

class alumno:
    nombre = input("Introduzca el nombre del alumn@: ")
    nota = float(input("Introduzca la nota del alumn@: "))
    def __init__(self):
        print("Nombre: ", self.nombre)
        print("Nota: ", self.nota)
    
    def calificacion(self):
        if self.nota >= 5:
            print("APROBADO")
        else:
            print("SUSPENDIDO")

if "__name__"=="__main__":
    alumno1 = alumno()
    alumno1.__init__()
    alumno1.calificacion()
    main()


