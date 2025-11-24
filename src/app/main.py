from fastapi import FastAPI
from app.application.TeacherController import router as teacher_router
from app.application.StudentController import router as student_router
from app.config.cors_config import setup_cors

app = FastAPI()

setup_cors(app)

# Aquí deben incluirse los routers
app.include_router(teacher_router)
app.include_router(student_router)

@app.get("/")
def root():
    return {"message": "API running"}
