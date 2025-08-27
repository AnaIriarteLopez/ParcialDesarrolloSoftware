from app import db
from app.models.universidad import Universidad

class UniversidadRepository:
    @staticmethod
    def crear_universidad(universidad):
        db.session.add(universidad)
        db.session.commit()

    @staticmethod
    def buscar_por_id(id: int):
        return db.session.query(Universidad).filter_by(id=id).first()

    @staticmethod
    def buscar_todos():
        return db.session.query(Universidad).all()

    @staticmethod
    def actualizar_universidad(universidad) -> Universidad:
        universidad_existente = db.session.merge(universidad)
        if not universidad_existente:
            return None
        return universidad_existente

    @staticmethod
    def borrar_universidad(id: int) -> Universidad:
        universidad = db.session.query(Universidad).filter_by(id=id).first()
        if not universidad:
            return None
        db.session.delete(universidad)
        db.session.commit()
        return False