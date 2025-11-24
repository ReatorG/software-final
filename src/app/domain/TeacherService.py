from fastapi import Depends, HTTPException
from app.infrastructure.TeacherRepository import TeacherRepository, Teacher


class TeacherService:

    def __init__(self, repo: TeacherRepository = Depends()):
        self.repo = repo

    # ===========================
    # LISTAR
    # ===========================
    def list_teachers(self):
        return self.repo.list_teachers()

    # ===========================
    # OBTENER
    # ===========================
    def get_teacher(self, teacher_id: str):
        teacher = self.repo.get_teacher(teacher_id)
        if not teacher:
            raise HTTPException(404, detail="Docente no encontrado")
        return teacher

    # ===========================
    # CREAR
    # ===========================
    def create_teacher(self, teacher: Teacher):
        # Si docente ya existe, consideramos error (distinto del repo)
        if self.repo.get_teacher(teacher.id):
            raise HTTPException(400, detail="El docente ya existe")

        return self.repo.create_teacher(teacher)

    # ===========================
    # ACTUALIZAR
    # ===========================
    def update_teacher(self, teacher_id: str, teacher: Teacher):
        existing = self.repo.get_teacher(teacher_id)
        if not existing:
            raise HTTPException(404, detail="Docente no encontrado para actualizar")

        updated = self.repo.update_teacher(teacher_id, teacher)
        return updated

    # ===========================
    # ELIMINAR
    # ===========================
    def delete_teacher(self, teacher_id: str):
        deleted = self.repo.delete_teacher(teacher_id)
        if not deleted:
            raise HTTPException(404, detail="Docente no encontrado para eliminar")

        return {"message": "Docente eliminado con éxito", "id": teacher_id}
