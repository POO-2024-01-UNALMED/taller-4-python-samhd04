from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, listadoAlumnos=None):
        self._grupo = grupo
        if asignaturas == None:
            self._asignaturas = [] 
        else:
            self._asignaturas = asignaturas
        if listadoAlumnos == None:
            self.listadoAlumnos = []
        else:
            self._asignaturas = listadoAlumnos

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(x)

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
