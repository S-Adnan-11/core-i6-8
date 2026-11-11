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

def student_count(records):
    students = {}
    for record in records:
        student_id = record[0]

        if student_id in students:
            students[student_id] += 1
        else:
            students[student_id] = 1

    return students

def activity_count(records):
    activities = {}
    for record in records:
        activity = record[1]

        if activity in activities:
            activities[activity] += 1
        else:
            activities[activity] = 1
    return activities 

def track_calls(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Number of calls - {count}")
        result = func(*args, **kwargs)
        return result
    return wrapper

@track_calls
def analyze_records(records):
    if not records:
        return 'No records'
    
    student_map = student_count(records)
    activity_map = activity_count(records)

    student_map_list = list(student_map.items())
    student_map_list.sort(key=lambda x: (x[1], x[0]), reverse=True)
    highest_count = student_map_list[0]

    return f'student_counts: {student_map}\nactivity_counts: {activity_map}\nmost_active_student: {highest_count[0]} '

print(analyze_records(records))
print(analyze_records(records))
print(analyze_records(records))



def count_student_records(records, student_id):
    if not records:
        return 0
    if student_id not in [record[0] for record in records]:
        return 0
    count = 0
    c_record = records[0] 
    r_records = records[1:]
    if c_record[0] == student_id:
        count += 1
    return count + count_student_records(r_records, student_id)

print(count_student_records(records, "ST01"))
print(count_student_records(records, "ST02"))
print(count_student_records(records, "ST03"))

    