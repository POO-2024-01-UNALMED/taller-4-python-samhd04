from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, listadoAlumnos=None):
        self._grupo = grupo
        if asignaturas == None:
            self._asignaturas = [] 
        if listadoAlumnos == None:
            self.listadoAlumnos = []

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            if self._asignaturas != None:
                self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if lista == None:
            lista = []
        self.listadoAlumnos = self.listadoAlumnos + lista
        self.listadoAlumnos.append(alumno) 

    def __str__(self):
        return "Grupo de estudiantes: " + self._grupo

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
