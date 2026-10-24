

groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЗИС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Мария",
        "surname": "Кузнецова",
        "exams": ["Информатика", "ЭЗИС", "Web"],
        "marks": [5, 4, 5]
    },
    {
        "name": "Дмитрий",
        "surname": "Соколов",
        "exams": ["История", "АиГ", "Философия"],
        "marks": [3, 3, 4]
    },
    {
        "name": "Анна",
        "surname": "Попова",
        "exams": ["ИС", "КТП", "Web"],
        "marks": [4, 5, 4]
    }
]


def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10),
          u"Экзамены".ljust(35), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15),
              student["surname"].ljust(10),
              str(student["exams"]).ljust(35),
              str(student["marks"]).ljust(20))


def average_mark(student):
    return sum(student["marks"]) / len(student["marks"])


def filter_by_average(students, threshold):
    result = []
    for student in students:
        if average_mark(student) > threshold:
            result.append(student)
    return result


def main():
    print("=== Все студенты группы ===\n")
    print_students(groupmates)

    # Ввод порога с клавиатуры (запятая тоже принимается)
    raw = input("\nВведите минимальный средний балл для фильтрации: ")
    try:
        threshold = float(raw.replace(",", "."))
    except ValueError:
        print("Ошибка: нужно ввести число (например, 4 или 4.5)")
        return

    filtered = filter_by_average(groupmates, threshold)

    print("\n=== Студенты со средним баллом выше %.2f ===\n" % threshold)
    if filtered:
        print_students(filtered)
    else:
        print("Студентов с таким средним баллом нет.")


if __name__ == "__main__":
    main()