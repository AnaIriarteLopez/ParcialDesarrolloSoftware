import unittest
from unittest.mock import MagicMock
from app.ficha_alumno.serializer import FichaAlumnoSerializer

class DummyFacultad:
    def __init__(self, nombre):
        self.nombre = nombre

class DummyAlumno:
    def __init__(self, nro_legajo, apellido, nombre, facultad):
        self.nro_legajo = nro_legajo
        self.apellido = apellido
        self.nombre = nombre
        self.facultad = facultad

class TestFichaAlumnoSerializer(unittest.TestCase):
    def test_serialize(self):
        facultad = DummyFacultad("Facultad de Ingeniería")
        alumno = DummyAlumno(123, "Pérez", "Juan", facultad)
        serializer = FichaAlumnoSerializer()
        result = serializer.serialize(alumno)
        self.assertEqual(result["nro_legajo"], 123)
        self.assertEqual(result["apellido"], "Pérez")
        self.assertEqual(result["nombre"], "Juan")
        self.assertEqual(result["facultad"], "Facultad de Ingeniería")

if __name__ == "__main__":
    unittest.main()
