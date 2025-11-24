from fastapi import Depends, HTTPException
from app.infrastructure.StudentRepository import StudentRepository
from app.domain.Student import Student


class StudentService:

    def __init__(self, repo: StudentRepository = Depends()):
        self.repo = repo

    # ===========================
    # LISTAR ESTUDIANTES
    # ===========================
    def list_students(self, teacher_id: str):
        return self.repo.list_students(teacher_id)

    # ===========================
    # OBTENER ESTUDIANTE
    # ===========================
    def get_student(self, teacher_id: str, student_id: str):
        student = self.repo.get_student(teacher_id, student_id)
        if not student:
            raise HTTPException(404, detail="Estudiante no encontrado")
        return student

    # ===========================
    # CREAR / REGISTRAR ESTUDIANTE
    # ===========================
    def create_student(self, teacher_id: str, student: Student):
        """
        Crea el estudiante si no existe. 
        Si ya existe, lanza error (distinto del repository).
        """
        if self.repo.get_student(teacher_id, student.id):
            raise HTTPException(400, detail="El estudiante ya existe")

        return self.repo.create_or_get_student(teacher_id, student.id)

    # ===========================
    # ACTUALIZAR ESTUDIANTE
    # ===========================
    def update_student(self, teacher_id: str, student_id: str, student: Student):
        existing = self.repo.get_student(teacher_id, student_id)
        if not existing:
            raise HTTPException(404, detail="Estudiante no encontrado para actualizar")

        # reemplaza completamente el objeto Student
        updated_student = Student(
            id=student_id,
            evaluations=student.evaluations,
            attendance_ok=student.attendance_ok,
            extra_points=student.extra_points
        )

        self.repo.students_by_teacher[teacher_id][student_id] = updated_student
        return updated_student

    # ===========================
    # ELIMINAR ESTUDIANTE
    # ===========================
    def delete_student(self, teacher_id: str, student_id: str):
        deleted = self.repo.delete_student(teacher_id, student_id)
        if not deleted:
            raise HTTPException(404, detail="Estudiante no encontrado para eliminar")

        return {"message": "Estudiante eliminado con éxito", "id": student_id}
