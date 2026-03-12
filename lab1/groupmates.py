groupmates = [
    {
        "name": u"Василий",
        "group": "912-1",
        "age": 19,
        "marks": [4, 3, 5, 5, 4]
    },
    {
        "name": u"Иван",
        "group": "912-1",
        "age": 19,
        "marks": [3, 3, 5, 5, 4]
    },
    {
        "name": u"Петя",
        "group": "912-2",
        "age": 19,
        "marks": [5, 3, 5, 5, 4]
    },
    {
        "name": u"Маша",
        "group": "912-2",
        "age": 19,
        "marks": [4, 5, 5, 5, 4]
    },
    {
        "name": u"Катя",
        "group": "912-3",
        "age": 19,
        "marks": [5, 5, 5, 5, 4]
    }
]

def print_students(students):
    print(u"Имя студента".ljust(15), \
          u"Группа".ljust(8), \
          u"Возраст".ljust(8), \
          u"Оценки".ljust(20))
    for student in students:
        print( \
            student["name"].ljust(15), \
            student["group"].ljust(8), \
            str(student["age"]).ljust(8), \
            str(student["marks"]).ljust(20))
    print("\n")

def filter_students_by_avg_mark(students, min_avg_mark):
    filtered = []

    for student in students:
        marks = student["marks"]
        if not marks:
            avg = 0.0
        else:
            avg = sum(marks) / len(marks)

        if avg > min_avg_mark:
            filtered.append(student)

    return filtered

print_students(filter_students_by_avg_mark(groupmates, 4.0))
