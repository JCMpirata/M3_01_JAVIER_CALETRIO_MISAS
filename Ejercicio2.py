from ast import main

class alumno:
    
    def __init__(self, alumno, nota):
        self.alumno = alumno
        self.nota = float(nota)

    def calificacion(self):
        for self.resultado in self.nota:
            if self.resultado >= 5:
                print("APROBADO")
            else:
                ("SUSPENDIDO")

    def __str__(self):
        cadena = "El alumno" + self.alumno + "ha sacado" + self.nota
        return cadena


if "__name__"=="__main__":
    alumno1 = alumno("Javier", 6.5)
    alumno2 = alumno("Pablo", 4.75)
    alumno3 = alumno("Adrian", 8.2)

    print(alumno1)
    print(alumno2)
    print(alumno3)
    main()
    