from fastapi import FastAPI
from app.config.cors_config import setup_cors
from app.application.StudentController import router as student_router

app = FastAPI()
setup_cors(app)

app.include_router(student_router)

@app.get("/")
def root():
    return {"message": "API funcionando sin base de datos"}
