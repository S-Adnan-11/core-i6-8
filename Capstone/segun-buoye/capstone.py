def analyze_records(records):
    student_counts = {}
    activity_counts = {}
    for record in records:
        student_counts[record[0]] = student_counts.get(record[0], 0)+1
        activity_counts[record[1]] = activity_counts.get(record[1], 0)+1

    count = 0
    most_active = None
    for student in student_counts:
        if student_counts[student] > count:
            count = student_counts[student]
            most_active = student
        if student_counts[student] == count:
            if student < most_active:
                most_active = student

    return student_counts, activity_counts, most_active


def count_student_records(records, student_id):
    if not records:
        return 0
    if isinstance(records, tuple):
        return 1 if records[0]==student_id else 0
    return count_student_records(records[0], student_id)+count_student_records(records[1:], student_id)


def track_calls(func):
    count = 0
    def wrapper(x):
        nonlocal count
        count += 1
        print(f"Number of calls - {count}")
        return func(x)
    return wrapper

@track_calls
def analyze_records_dec(records):
    student_counts = {}
    activity_counts = {}
    for record in records:
        student_counts[record[0]] = student_counts.get(record[0], 0)+1
        activity_counts[record[1]] = activity_counts.get(record[1], 0)+1

    count = 0
    most_active = None
    for student in student_counts:
        if student_counts[student] > count:
            count = student_counts[student]
            most_active = student
        if student_counts[student] == count:
            if int(student[-2:]) < int(most_active[-2:]):
                most_active = student

    return student_counts, activity_counts, most_active

    
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

print(count_student_records(records, "ST01"))
# student_counts, activity_counts, most_active = analyze_records_dec(records)
# student_counts, activity_counts, most_active = analyze_records_dec(records)
# print(student_counts)
# print(activity_counts)
# print(most_active)

