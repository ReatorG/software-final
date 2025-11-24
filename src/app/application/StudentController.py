from fastapi import APIRouter, Depends
from app.domain.StudentService import StudentService
from app.domain.Student import Student

router = APIRouter(prefix="/api/students", tags=["Students"])

# ===============================
# LISTAR ESTUDIANTES DE UN DOCENTE
# ===============================
@router.get("/{teacher_id}")
def list_students(teacher_id: str, service: StudentService = Depends()):
    return service.list_students(teacher_id)

# ===============================
# OBTENER ESTUDIANTE
# ===============================
@router.get("/{teacher_id}/{student_id}")
def get_student(teacher_id: str, student_id: str, service: StudentService = Depends()):
    return service.get_student(teacher_id, student_id)

# ===============================
# CREAR ESTUDIANTE
# ===============================
@router.post("/{teacher_id}")
def create_student(teacher_id: str, student: Student, service: StudentService = Depends()):
    return service.create_student(teacher_id, student)

# ===============================
# ACTUALIZAR ESTUDIANTE
# ===============================
@router.put("/{teacher_id}/{student_id}")
def update_student(teacher_id: str, student_id: str, student: Student, service: StudentService = Depends()):
    return service.update_student(teacher_id, student_id, student)

# ===============================
# ELIMINAR ESTUDIANTE
# ===============================
@router.delete("/{teacher_id}/{student_id}")
def delete_student(teacher_id: str, student_id: str, service: StudentService = Depends()):
    return service.delete_student(teacher_id, student_id)
