from app.models.alumno import Alumno
from app.models.facultad import Facultad

class FichaAlumnoService:
    def get_ficha(self, legajo):
        alumno = Alumno.query.filter_by(nro_legajo=legajo).first()
        if not alumno:
            return None
        return alumno
