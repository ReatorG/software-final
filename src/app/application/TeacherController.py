from fastapi import APIRouter, Depends
from app.domain.TeacherService import TeacherService
from app.infrastructure.TeacherRepository import Teacher

router = APIRouter(prefix="/api/teachers", tags=["Teachers"])

# ===============================
# LISTAR DOCENTES
# ===============================
@router.get("/")
def list_teachers(service: TeacherService = Depends()):
    return service.list_teachers()

# ===============================
# OBTENER DOCENTE
# ===============================
@router.get("/{teacher_id}")
def get_teacher(teacher_id: str, service: TeacherService = Depends()):
    return service.get_teacher(teacher_id)

# ===============================
# CREAR DOCENTE
# ===============================
@router.post("/")
def create_teacher(teacher: Teacher, service: TeacherService = Depends()):
    return service.create_teacher(teacher)

# ===============================
# ACTUALIZAR DOCENTE
# ===============================
@router.put("/{teacher_id}")
def update_teacher(teacher_id: str, teacher: Teacher, service: TeacherService = Depends()):
    return service.update_teacher(teacher_id, teacher)

# ===============================
# ELIMINAR DOCENTE
# ===============================
@router.delete("/{teacher_id}")
def delete_teacher(teacher_id: str, service: TeacherService = Depends()):
    return service.delete_teacher(teacher_id)
