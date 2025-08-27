from flask import Blueprint, request, jsonify, send_file
from app.ficha_alumno.service import FichaAlumnoService
from app.ficha_alumno.serializer import FichaAlumnoSerializer
from app.ficha_alumno.pdf_generator import FichaAlumnoPDFGenerator
import tempfile
import os

ficha_alumno_bp = Blueprint('ficha_alumno', __name__)

@ficha_alumno_bp.route('/ficha_alumno/<int:legajo>', methods=['GET'])
def get_ficha_alumno(legajo):
    service = FichaAlumnoService()
    serializer = FichaAlumnoSerializer()
    pdf_generator = FichaAlumnoPDFGenerator()
    alumno = service.get_ficha(legajo)
    if not alumno:
        return jsonify({'error': 'Alumno no encontrado'}), 404
    ficha_json = serializer.serialize(alumno)
    formato = request.args.get('formato', 'json')
    if formato == 'pdf':
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp:
            pdf_generator.generate(ficha_json, tmp.name)
            tmp.close()
            response = send_file(tmp.name, as_attachment=True, download_name=f"ficha_alumno_{legajo}.pdf")
            # Eliminar el archivo temporal después de enviar
            @response.call_on_close
            def cleanup():
                os.remove(tmp.name)
            return response
    return jsonify(ficha_json)
