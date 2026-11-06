"""A school records activities completed by students. 
Each record is a tuple containing a student ID and an activity name. 
Your program must summarize the records, answer a recursive counting query, 
and track how often the main analysis function is called."""


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

"""QUEST 2 — Build the analysis engine (25 marks)
Implement analyze_records(records). It must return:
    • A dictionary mapping each student ID to the number of records for that student.
    • A dictionary mapping each activity name to the number of times that activity appears.
    • The ID of the student with the most records, or None when there are no records.
Rules:
    • Use dictionaries as hash maps. Do not use collections.Counter.
    • Handle an empty records list without crashing.
    • If students tie for the highest count, choose the lexicographically smallest student ID and document that rule.
    • Keep the function readable; use descriptive variable names.
Expected result for the sample data:
student_counts = {
    "ST01": 4,
    "ST02": 2,
    "ST03": 2
}
activity_counts = {
    "Python": 3,
    "HTML": 2,
    "CSS": 2,
    "JavaScript": 1
}
most_active_student = "ST01" """

def analyze_records(records: list[tuple[str, str]]) -> tuple[dict[str, int], dict[str, int], str|None]:
    student_counts = {}
    activity_counts = {}
    most_active_student = None
    highest_activity = 0

    for student_id, activity in records:
        student_counts.setdefault(student_id, 0)
        student_counts[student_id] += 1

        if highest_activity < student_counts[student_id]:
            most_active_student = student_id
            highest_activity = student_counts[student_id]
        elif highest_activity == student_counts[student_id]:
            # If there are more than one most active students
            # return the alphabetically first student ID
            # min returns the lexiographically smallest string
            # among the passed string values
            most_active_student = min(most_active_student, student_id)

        activity_counts.setdefault(activity, 0)
        activity_counts[activity] += 1


    return student_counts, activity_counts, most_active_student


"""Explain: How does the dictionary update work when a key 
is seen for the first time versus when it appears again?"""

"""Using setdefault: setdefault sets the key to the default value when the 
key has not been set, otherwise it leaves the key unchanged."""


"""QUEST 3 — Add recursion (20 marks)
Implement count_student_records(records, student_id) recursively.
Requirements:
    • Do not use for or while loops inside this function.
    • Do not use sum(), list.count(), or comprehensions.
    • Return 0 when the records list is empty.
    • Count every record whose student ID matches student_id.
    • Do not modify the original records list.
Expected examples:
count_student_records(records, "ST01")  # 4
count_student_records(records, "ST02")  # 2
count_student_records(records, "ST99")  # 0
count_student_records([], "ST01")      # 0"""

def count_student_records(records: list[tuple[str, str]], student_id: str) -> int:
    if len(records) == 0:
        return 0

    if records[0][0] == student_id:
        return 1 + count_student_records(records[1:], student_id)
    else:
        return count_student_records(records[1:], student_id)

"""Explain your recursion: 
Identify the base case, 
the recursive step, 
and how the problem gets smaller on each call. 
What resource limit could affect this function on a very large list?"""

"""
The base case is when the list has a length of 0.
if len(records) == 0:
        return 0

The recursive step adds 1 or nothing while calling the function
on the list without the first element.

The list looses its first element with every call down the stack.
Eventually it will reach an empty list.

Python has a recursion call stack limit of 1000.
If the records list has 1000 or more elements it will hit the limit
unless the limit is manually removed.
"""


"""QUEST 4 — Add a decorator (20 marks)
Implement a decorator named track_calls and apply it to analyze_records.
The decorator must:
    • Increment a persistent counter each time the decorated function is called.
    • Work with positional and keyword arguments.
    • Return the original function's result unchanged.
    • Make the current count accessible or print it clearly.
    • Keep the counter across separate calls."""

def track_calls(f: function) -> function:
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        result = f(*args, **kwargs)
        return result
    wrapper.count = 0
    return wrapper

"""Explain: 
What does the wrapper add? 
Why must it return the result? 
What would break if the wrapper forgot to return anything?"""

"""
It adds a counter
It must return the result so that the function keeps behaving
the same way it did before being decorated.
The wrapped function would stop returning changing its behaviour
instead of adding to it.
"""

"""QUEST 6 — Defend your Big O analysis (10 marks)
A. Main analyzer: 
State expected time complexity in terms of n records 
and explain which operations are performed for each record."""

"""
analyze_records - O(n)
A single run through the records and all operations in it a O(1)

count_student_records - O(n)
It goes through the whole records list.
"""

"""B. Extra space: 
Explain how the number of unique student IDs and 
activity names affects memory use."""

"""
The more unique IDs and activity names the bigger the student_count 
and activity_count lists in analyze_records.
count_student_records is not affected by the amount of unique IDs 
and activity names.
"""

"""C. Recursive counter: 
State its time complexity and auxiliary space complexity. 
Explain why the recursive calls use additional stack space."""

"""
Time complexity - O(n)
Space complexity - O(n)

Python needs to know which function call called which to know
where to return the value of each call. It uses a call stack to
manage this. This means recursive functions have a side effect of
having at least O(n) space complexity.
"""

"""D. Hash map caveat: 
Explain why dictionary operations are usually expected O(1), 
not guaranteed O(1) in every possible case, 
and what severe collision behavior can do."""


"""
Collision.
When two keys return the same index number when hashed.

A dictionary without any colliding keys, a well maintained dictionary
has a operation time complexity of O(1).

The more key collisions the more the time complexity tends to O(n)
as the dictionary becomes an array/linked-list.
"""

if __name__ == "__main__":
    # print(count_student_records(records, "ST02"))
    # print(count_student_records(records, "ST01"))
    # print(count_student_records(records, "ST99"))
    # print(count_student_records([], "ST01"))


    # Tests
    # Empty records -> Both count dictionaries empty; most active is None
    print(analyze_records([]))
    # One record -> Student and activity counts are 1
    print(analyze_records([("ST01", "Python")]))
    # Repeated student/activity -> Counts reflect every occurrence
    print(analyze_records([("ST01", "Python"), ("ST01", "Python"), ("ST01", "Python")]))
    # Unknown student ID -> Recursive count returns 0
    print(count_student_records([("ST01", "Python")], "Unknown student ID"))
    # Tied student counts -> Lexicographically smallest ID wins
    print(analyze_records([("ST01", "Python"), ("ST02", "Python"), ("ST03", "Python")]))
    # Three analysis calls -> Decorator counter ends at 3
    analyze_records = track_calls(analyze_records)
    analyze_records([])
    analyze_records([])
    analyze_records([])
    print(analyze_records.count)
    # Regular Test
    print(analyze_records(records))




