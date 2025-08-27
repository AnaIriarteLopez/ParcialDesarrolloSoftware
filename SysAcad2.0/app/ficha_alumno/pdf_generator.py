from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class FichaAlumnoPDFGenerator:
    def generate(self, alumno_data, file_path):
        c = canvas.Canvas(file_path, pagesize=letter)
        c.setFont("Helvetica", 12)
        y = 750
        c.drawString(100, y, f"Ficha del Alumno")
        y -= 30
        for key, value in alumno_data.items():
            c.drawString(100, y, f"{key}: {value}")
            y -= 20
        c.save()
