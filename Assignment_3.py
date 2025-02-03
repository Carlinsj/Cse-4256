def high_grades(di):
    result = {}
    for student, grades in di.items():
        result[student] = sum(1 for grade in grades if grade >= 90)
    return result


