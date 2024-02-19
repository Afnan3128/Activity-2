import pytest
from main import StudentsInMLOps

@pytest.fixture
def student_manager():
    return StudentsInMLOps()

def test_enrollStudents(student_manager):
    student_manager.enrollStudents(5)
    assert student_manager.getTotalStrength() == 5

def test_dropStudents(student_manager):
    student_manager.enrollStudents(10)
<<<<<<< HEAD
    student_manager.dropStudents(4)
    assert student_manager.getTotalStrength() == 6
=======
    student_manager.dropStudents(2)
    assert student_manager.getTotalStrength() == 8
>>>>>>> dc41609ec5bd1c3dd04cab9bd4d08dd1e01075c5

def test_getTotalStrength(student_manager):
    student_manager.enrollStudents(8)
    assert student_manager.getTotalStrength() == 8

def test_getClassName(student_manager):
    assert student_manager.getClassName() == "StudentsInMLOps"
