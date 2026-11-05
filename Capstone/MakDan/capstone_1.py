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

def analyze_records(records):
    # empty records
    if not records:
        raise ValueError("records cannot be empty")
    
    student_counts = {}
    activity_counts = {}

    for id, activity in records:
        student_counts[id] = student_counts.get(id, 0) + 1
        activity_counts[activity] = activity_counts.get(activity, 0) + 1

    # sorting the dictionaries
    student_counts = dict(sorted(student_counts.items(), key=lambda item: (-item[1], item[0])))
    activity_counts = dict(sorted(activity_counts.items(), key=lambda item: (-item[1], item[0])))
    result = f"most_active_student = '{next(iter(student_counts))}'"

    return (
        student_counts, 
        activity_counts, 
        result
        )

print(analyze_records(records))


def count_student_records(records, student_id):
    # empty records
    if not records:
        return 0
    
    match = 1 if records[0][0] == student_id else 0
    
    return match + count_student_records(records[1:], student_id)


print(count_student_records(records, "ST01"))
print(count_student_records(records, "ST02"))
print(count_student_records(records, "ST99"))
print(count_student_records([], "ST01"))