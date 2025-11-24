import pytest
from app.infrastructure.StudentRepository import StudentRepository
from app.domain.Student import Student


def test_create_or_get_student():
    repo = StudentRepository()

    student = repo.create_or_get_student("prof1", "alu01")

    assert student.id == "alu01"
    assert student.attendance_ok is True
    assert student.extra_points == 0
    assert student.evaluations == []


def test_get_student_returns_none():
    repo = StudentRepository()

    student = repo.get_student("prof1", "unknown")

    assert student is None


def test_list_students():
    repo = StudentRepository()

    repo.create_or_get_student("prof1", "alu01")
    repo.create_or_get_student("prof1", "alu02")

    students = repo.list_students("prof1")

    assert len(students) == 2
    ids = {s.id for s in students}
    assert ids == {"alu01", "alu02"}


def test_delete_student():
    repo = StudentRepository()

    repo.create_or_get_student("prof1", "alu01")

    deleted = repo.delete_student("prof1", "alu01")
    assert deleted is True

    # Intentar eliminar otra vez
    deleted_again = repo.delete_student("prof1", "alu01")
    assert deleted_again is False
