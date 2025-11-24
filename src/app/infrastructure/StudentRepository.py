from app.domain.Student import Student
from typing import Dict


class StudentRepository:

    def __init__(self):
        # Base de datos en memoria
        # Estructura reducida y exclusiva para estudiantes:
        # {
        #     "teacher_id": {
        #         "student_id": Student(...)
        #     }
        # }
        self.students_by_teacher: Dict[str, Dict[str, Student]] = {}

    # -------------------------------
    # Helpers internos
    # -------------------------------
    def _get_teacher_students(self, teacher_id: str) -> Dict[str, Student]:
        """
        Obtiene (o crea si no existe) el diccionario de estudiantes
        asociados a un docente.
        """
        return self.students_by_teacher.setdefault(teacher_id, {})

    # -------------------------------
    # CRUD exclusivo para estudiantes
    # -------------------------------
    def create_or_get_student(self, teacher_id: str, student_id: str) -> Student:
        """
        Crea un estudiante vacío si no existe, o simplemente lo retorna.
        """
        teacher_students = self._get_teacher_students(teacher_id)
        return teacher_students.setdefault(student_id, Student(id=student_id))

    def get_student(self, teacher_id: str, student_id: str) -> Student | None:
        """
        Retorna un estudiante o None si no existe.
        """
        teacher_students = self._get_teacher_students(teacher_id)
        return teacher_students.get(student_id)

    def list_students(self, teacher_id: str):
        """
        Lista todos los estudiantes registrados para un docente.
        """
        teacher_students = self._get_teacher_students(teacher_id)
        return list(teacher_students.values())

    def delete_student(self, teacher_id: str, student_id: str) -> bool:
        """
        Elimina un estudiante. Retorna True si existía, False si no existía.
        """
        teacher_students = self._get_teacher_students(teacher_id)
        if student_id in teacher_students:
            del teacher_students[student_id]
            return True
        return False
