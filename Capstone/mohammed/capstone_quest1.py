# Quest 1 

"""
A function to create a dictinoary maaping student ID'S to the number of records 

A function to create a dictionary mapping activity name to the number of times it appears

Each Dictionary key represents a unique student_id in the records, and the value is a list containing each student activities.  Dictionary is the optimal DS because it aids fast lookup and write operation of each student_id
"""

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

# Quest 2
 
def student_count(records):
    student_map = {}

    for record in records:
        student_id = record[0]

        if student_id not in student_map:
            student_map[student_id] = 1
        else:
            student_map[student_id] += 1

    return student_map

def activity_count(records):
    activity_map = {}
    for record in records:
        activity = record[1]

        if activity not in activity_map:
            activity_map[activity] = 1
        else:
            activity_map[activity] += 1

    return activity_map

def analyze_records(records: list[tuple[str, str]]):
    n = len(records)

    if n == 0:
        return "Empty Records"

    student_map = student_count(records)
    activity_map = activity_count(records)

    student_map_list = list(student_map.items())
    student_map_list.sort(key=lambda x: (x[1], x[0]), reverse=True)
    highest_count = student_map_list[0]

    return {
        "student_count": f"{student_map}",
        "activity_count": f"{activity_map}",
        "most_active_count": f"{highest_count}"
    }

print(analyze_records(records))

# Quest 3 
def count_student_records_recursively(records, student_id):
    if len(records) == 0 or student_id not in records:
        return 0

    current_record = records[0]
    remaining_records = records[1:]

    if current_record[0] == student_id:
        return 1 + count_student_records_recursively(remaining_records, student_id)
    else:
        return count_student_records_recursively(remaining_records, student_id)


"""
The base case checks if the records list is empty. Each recursive case reduces the number of items in records by slicing from the first index.

"""


# Quest 4
def track_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1 
        return func(*args, **kwargs)

    wrapper.call_count = 0 
    return wrapper

analyzed_records = track_calls(analyze_records)
analyzed_records(records)
print(analyzed_records.call_count)
analyzed_records(records)
print(analyzed_records.call_count)
analyzed_records(records)
print(analyzed_records.call_count)

print(count_student_records_recursively(records, "ST02"))

"""
The wrapper increment the call_count attribute anytime the passed function to track_calls get called.
"""

