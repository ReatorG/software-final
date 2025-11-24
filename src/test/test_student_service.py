import pytest
from fastapi import HTTPException

from app.domain.StudentService import StudentService
from app.infrastructure.StudentRepository import StudentRepository
from app.domain.Student import Student


def create_service():
    repo = StudentRepository()
    return StudentService(repo)


def test_create_student_success():
    service = create_service()

    student = Student(id="alu01")
    created = service.create_student("prof1", student)

    assert created.id == "alu01"
    assert created.evaluations == []
    assert created.attendance_ok is True


def test_create_student_already_exists():
    service = create_service()

    service.create_student("prof1", Student(id="alu01"))

    with pytest.raises(HTTPException):
        service.create_student("prof1", Student(id="alu01"))


def test_get_student_exists():
    service = create_service()

    service.create_student("prof1", Student(id="alu01"))
    student = service.get_student("prof1", "alu01")

    assert student.id == "alu01"


def test_get_student_not_found():
    service = create_service()

    with pytest.raises(HTTPException):
        service.get_student("prof1", "unknown")


def test_list_students():
    service = create_service()

    service.create_student("prof1", Student(id="alu01"))
    service.create_student("prof1", Student(id="alu02"))

    students = service.list_students("prof1")
    assert len(students) == 2


def test_delete_student():
    service = create_service()

    service.create_student("prof1", Student(id="alu01"))

    result = service.delete_student("prof1", "alu01")
    assert result["id"] == "alu01"

    with pytest.raises(HTTPException):
        service.delete_student("prof1", "alu01")
