records = [
    ("ST01", "Python"),
    ("ST02", "HTML"),
    ("ST01", "Python"),
    ("ST03", "CSS"),
    ("ST02", "HTML"),
    ("ST01", "JavaScript"),
    ("ST03", "CSS"),
    ("ST01", "Python"),
]


def track_calls(func):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        result = func(*args, **kwargs)
        count += 1
        print(count)
        return result
    return wrapper


@track_calls
def analyze_records(records):
    activity_dict, student_dict = {}, {}

    for record in records:
        activity_dict[record[1]] = activity_dict.get(record[1], 0) + 1
        student_dict[record[0]] = student_dict.get(record[0], 0) + 1
    most_active_student = sorted(student_dict.items(), key=lambda x: (-x[1], x[0]))[0]

    return most_active_student[0]


def count_student_records(records, student):
    if not records:
        return 0
    counts = 1 if records[0][0] == student else 0
    return counts + count_student_records(records[1:], student)


print(analyze_records(records))
print(count_student_records(records, "ST01"))
print(count_student_records(records, "ST02"))
print(count_student_records(records, "ST99"))
print(count_student_records([], "ST01"))
print("")
print(analyze_records(records))
print(analyze_records(records))
print(analyze_records(records))
