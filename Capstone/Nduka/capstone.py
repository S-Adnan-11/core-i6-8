def analyze_records(records):
    activity_counts={}
    student_counts={}
    most_active=""
    most_active_count=0
    for id,course in records:
        student_counts[id]=student_counts.get(id,0)+1
        activity_counts[course]=activity_counts.get(course,0)+1
        if student_counts[id]>most_active_count:
            most_active_count=student_counts[id]
            most_active=id
        elif student_counts[id]==most_active_count:
            if most_active>id:
                most_active=id
    if not most_active:
        most_active=None
    return student_counts,activity_counts,most_active

def count_student_records(records,student_id):
    count=0
    if not records:
        return 0
    if records[0][0]==student_id:
        count+=1
    count+=count_student_records(records[1:],student_id)
    
    return count

def track_calls(func):
    count=0
    
    def wrapper(record):
        nonlocal count
        count+=1
        print(f"Called {count} times")
        return func(record)
    return wrapper
analyze_records=track_calls(analyze_records)


def display(record_dic,prompt):
    k=1
    if record_dic:
        print(prompt)
    else:
        print("No Records")
    for key,value in record_dic.items():
        print(f"{k}. {key} {value}")
        k+=1


records = [
    # ("ST01", "Python"),
    # ("ST02", "HTML"),
    # ("ST01", "Python"),
    # ("ST03", "CSS"),
    # ("ST02", "HTML"),
    # ("ST01", "JavaScript"),
    # ("ST03", "CSS"),
    # ("ST01", "Python")
    # ("ST02","Java"),
    # ("ST02","Go")
]

student_counts,activity_counts,most_active=analyze_records(records)
# student_counts,activity_counts,most_active=analyze_records(records)
# student_counts,activity_counts,most_active=analyze_records(records)



display(student_counts,"Student Counts")
display(activity_counts,"Activity Counts")
print(most_active)
print(count_student_records(records,"ST01"))


"""
I understand recursion better, but the decorator still seems a bit blur

if the records grew to one million or even 1000 
i would change my recursive count to iterative count
so as not to get to maximum recursive depth error
"""
