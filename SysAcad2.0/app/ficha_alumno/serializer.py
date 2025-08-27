class FichaAlumnoSerializer:
    def serialize(self, alumno):
        return {
            "nro_legajo": alumno.nro_legajo,
            "apellido": alumno.apellido,
            "nombre": alumno.nombre,
            "facultad": alumno.facultad.nombre if alumno.facultad else None
        }
