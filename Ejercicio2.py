from ast import main

class alumno:
    alumno1 = input("Introduzca el nombre del alumn@: ")
    nota1 = float(input("Introduzca la nota del alumn@: "))
    alumno2 = input("Introduzca el nombre del alumn@: ")
    nota2 = float(input("Introduzca la nota del alumn@: "))
    alumno3 = input("Introduzca el nombre del alumn@: ")
    nota3 = float(input("Introduzca la nota del alumn@: "))

    def __init__(self):
        print("Nombre: ", self.alumno1)
        print("Nota: ", self.nota1)
        print("Nombre: ", self.alumno2)
        print("Nota: ", self.nota2)
        print("Nombre: ", self.alumno3)
        print("Nota: ", self.nota3)

    def calificacion(self):
        for self.nota in self.nota1, self.nota2, self.nota3:
            if self.nota >= 5:
                print("APROBADO")
            else:
                ("SUSPENDIDO")


if "__name__"=="__main__":
    alumno1 = alumno()
    alumno1.__init__()
    alumno1.calificacion()
    main()
    