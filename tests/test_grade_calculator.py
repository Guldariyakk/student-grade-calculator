import pytest

from src.grade_calculator import calculate_average, get_letter_grade, is_passed


def test_calculate_average():
    assert calculate_average([85, 90, 78, 92]) == 86.25


def test_letter_grade_a():
    assert get_letter_grade(95) == "A"


def test_letter_grade_b():
    assert get_letter_grade(85) == "B"


def test_letter_grade_f():
    assert get_letter_grade(40) == "F"


def test_student_passed():
    assert is_passed(75) is True


def test_student_failed():
    assert is_passed(50) is False


def test_empty_grades_raise_error():
    with pytest.raises(ValueError):
        calculate_average([])


def test_invalid_grade_raises_error():
    with pytest.raises(ValueError):
        calculate_average([85, 105, 90])


def test_invalid_score_raises_error():
    with pytest.raises(ValueError):
        get_letter_grade(-5)
