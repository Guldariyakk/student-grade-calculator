from src.grade_calculator import calculate_average, get_letter_grade, is_passed


def main():
    student = "Aigerim"
    grades = [85, 90, 78, 92]

    average = calculate_average(grades)
    letter = get_letter_grade(average)
    result = "Сдал" if is_passed(average) else "Не сдал"

    print("=== Расчёт успеваемости студента ===")
    print()
    print(f"Студент: {student}")
    print(f"Оценки: {grades}")
    print(f"Средний балл: {average:.2f}")
    print(f"Буквенная оценка: {letter}")
    print(f"Результат: {result}")


if __name__ == "__main__":
    main()
