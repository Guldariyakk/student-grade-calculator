"""Функции для расчёта успеваемости студента."""


def calculate_average(grades):
    """Вычисляет средний балл по списку оценок."""
    if not grades:
        raise ValueError("Список оценок не может быть пустым")

    for grade in grades:
        if grade < 0 or grade > 100:
            raise ValueError("Оценка должна быть от 0 до 100")

    return sum(grades) / len(grades)


def get_letter_grade(score):
    """Возвращает буквенную оценку (A, B, C, D, F) по баллу."""
    if score < 0 or score > 100:
        raise ValueError("Балл должен быть от 0 до 100")

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def is_passed(score):
    """Возвращает True, если студент сдал (балл 60 и выше)."""
    return score >= 60
