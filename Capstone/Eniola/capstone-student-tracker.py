##########
# QUEST 1 — Design before coding
##########

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

##########
# QUEST 2 — Build the analysis engine
##########

def analyze_records(records):
  student_counts = {}
  activity_counts = {}

  for student_id, activity in records:
    # Count student records
    if student_id in student_counts:
      student_counts[student_id] += 1
    else:
      student_counts[student_id] = 1

    # Count activity occurrences
    if activity in activity_counts:
      activity_counts[activity] += 1
    else:
      activity_counts[activity] = 1

  # Identify the most active student
  most_active_student = None
  highest_count = 0

  for student_id, count in student_counts.items():
    if count > highest_count:
      highest_count = count
      most_active_student = student_id

    elif count == highest_count:
      if student_id < most_active_student:
        most_active_student = student_id

  return {
    "student_counts": student_counts,
    "activity_counts": activity_counts,
    "most_active_student": most_active_student
  }


##########
# QUEST 3 — Recursion
##########

def count_student_records(records, student_id):
  # Base case
  if len(records) == 0:
    return 0

  # Start the count at zero
  current_count = 0

  # Check whether the first record belongs to the student
  if records[0][0] == student_id:
    current_count = 1

  # Count the remaining records recursively
  remaining_count = count_student_records(records[1:], student_id)

  # Add the current record's count to the remaining count
  total_count = current_count + remaining_count

  return total_count


##########
# QUEST 4 — Decorators
##########

def track_calls(func):
  
  def wrapper(*args, **kwargs):
    wrapper.call_count += 1
    result = func(*args, **kwargs)
    return result

  wrapper.call_count = 0

  return wrapper


##########
# QUEST 5 — Testing
##########

# Test 1: Empty records
result = analyze_records([])

assert result == {
  "student_counts": {},
  "activity_counts": {},
  "most_active_student": None
}

# Test 2: One record
result = analyze_records([("ST01", "Python")])

assert result["student_counts"] == {"ST01": 1}
assert result["activity_counts"] == {"Python": 1}
assert result["most_active_student"] == "ST01"

# Test 3: Repeated records
records = [
  ("ST01", "Python"),
  ("ST01", "Python"),
  ("ST02", "HTML")
]

result = analyze_records(records)

assert result["student_counts"] == {
  "ST01": 2,
  "ST02": 1
}

assert result["activity_counts"] == {
  "Python": 2,
  "HTML": 1
}

# Test 4: Unknown student
records = [("ST01", "Python")]
assert count_student_records(records, "ST99") == 0

# Test 5: Tied student counts
records = [
  ("ST02", "HTML"),
  ("ST01", "Python"),
  ("ST02", "CSS"),
  ("ST01", "JavaScript")
]

result = analyze_records(records)
assert result["most_active_student"] == "ST01"

# Test 6: Decorator call count
@track_calls
def add(a, b):
  return a + b

assert add(2, 3) == 5
assert add(a=4, b=6) == 10
assert add(7, 8) == 15

assert add.call_count == 3

print("All tests passed!")