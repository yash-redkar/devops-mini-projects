import pytest

from app import calculate_average, assign_grade, get_result


def test_calculate_average():
    assert calculate_average([80, 90, 100]) == 90


def test_empty_marks_list():
    with pytest.raises(ValueError):
        calculate_average([])


def test_assign_grade_a():
    assert assign_grade(95) == "A"


def test_assign_grade_b():
    assert assign_grade(80) == "B"


def test_assign_grade_c():
    assert assign_grade(65) == "C"


def test_assign_grade_d():
    assert assign_grade(45) == "D"


def test_assign_grade_f():
    assert assign_grade(30) == "F"


def test_get_result():
    result = get_result([70, 80, 90])

    assert result["average"] == 80
    assert result["grade"] == "B"
