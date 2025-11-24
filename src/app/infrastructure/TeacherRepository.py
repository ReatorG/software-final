from dataclasses import dataclass, field
from typing import Dict, Optional
from datetime import datetime
from app.domain.Teacher import Teacher


class TeacherRepository:

    def __init__(self):
        # Base de datos en memoria solo para docentes:
        # {
        #     "teacher_id": Teacher(...)
        # }
        self.teachers: Dict[str, Teacher] = {}

    # -------------------------------
    # CREATE / INSERT
    # -------------------------------
    def create_teacher(self, teacher: Teacher) -> Teacher:
        """
        Crea un docente si no existe.
        """
        if teacher.id in self.teachers:
            return self.teachers[teacher.id]

        # created_at ya viene con default_factory -> datetime.utcnow
        self.teachers[teacher.id] = teacher
        return teacher

    # -------------------------------
    # GET / SELECT ONE
    # -------------------------------
    def get_teacher(self, teacher_id: str) -> Optional[Teacher]:
        """
        Obtiene un docente o None si no existe.
        """
        return self.teachers.get(teacher_id)

    # -------------------------------
    # SELECT ALL
    # -------------------------------
    def list_teachers(self):
        """
        Lista todos los docentes registrados.
        """
        return list(self.teachers.values())

    # -------------------------------
    # UPDATE
    # -------------------------------
    def update_teacher(self, teacher_id: str, updated_teacher: Teacher) -> Optional[Teacher]:
        """
        Actualiza un docente existente.
        """
        if teacher_id not in self.teachers:
            return None

        # Reemplaza completamente la instancia
        self.teachers[teacher_id] = updated_teacher
        return updated_teacher

    # -------------------------------
    # DELETE
    # -------------------------------
    def delete_teacher(self, teacher_id: str) -> bool:
        """
        Elimina un docente. Retorna True si existía.
        """
        if teacher_id in self.teachers:
            del self.teachers[teacher_id]
            return True

        return False
