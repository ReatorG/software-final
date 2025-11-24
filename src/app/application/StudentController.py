from fastapi import APIRouter, Depends
from app.domain.Student import Evaluation
from app.domain.StudentService import StudentService

router = APIRouter(prefix="/api/students", tags=["Students"])

@router.post("/{teacher_id}/{student_id}/evaluations")
def add_evaluation(teacher_id: str, student_id: str, eval: Evaluation, service: StudentService = Depends()):
    return service.add_evaluation(teacher_id, student_id, eval)

@router.post("/{teacher_id}/{student_id}/attendance")
def set_attendance(teacher_id: str, student_id: str, attendance_ok: bool, service: StudentService = Depends()):
    return service.set_attendance(teacher_id, student_id, attendance_ok)

@router.post("/{teacher_id}/{student_id}/extra")
def give_extra(teacher_id: str, student_id: str, year: int, points: float, service: StudentService = Depends()):
    return service.give_extra_points(teacher_id, student_id, year, points)

@router.get("/{teacher_id}/{student_id}/final-grade")
def final_grade(teacher_id: str, student_id: str, service: StudentService = Depends()):
    return service.calculate_final_grade(teacher_id, student_id)
