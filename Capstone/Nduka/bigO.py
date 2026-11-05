"""
Method one becomes very inefficient for worst case scenerio 
i.e no duplicates O(n2) (slightly faster than O(n2) actually)
However on average it does search at a manageable time rate
it seems to be the fasted when the first two items are the duplicates

Method 3 seems to be the fasted method for worst case scenerior of sorted list. 
if the list is not sorted it becomes the slowest method on average

Method 2 seems to be fasted on average.  but does more work memory wise

"""

import random
import time

def has_duplicate_a(items):
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j]:
                return True
    return False

def has_duplicate_b(items):
    seen = set()
    for item in items:
        if item in seen:
            return True
        seen.add(item)
    return False

def has_duplicate_c(items):
    items = sorted(items)
    for i in range(1, len(items)):
        if items[i] == items[i - 1]:
            return True
    return False

def generate(n):
    result=[]
    for i in range(n+1):
        # result.append(random.randint(1,10000))
        result.append(i)
    return [0]+result

items=generate(20000)

start=time.time()
has_duplicate_a(items)
end=time.time()
print("has_duplicate_a: ",end-start)

start=time.time()
has_duplicate_b(items)
end=time.time()
print("has_duplicate_b: ",end-start)

start=time.time()
has_duplicate_c(items)
end=time.time()
print("has_duplicate_c: ",end-start)

