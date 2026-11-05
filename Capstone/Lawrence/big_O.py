
#  (A). Analyze the three implementations
# Implementation A — Nested loops

def has_duplicate_a(items):
   for i in range(len(items)):
       for j in range(i + 1, len(items)):
           if items[i] == items[j]:
               return True
   return False


"""Time complexity: O(n²)

Reason:
The outer loop visits each element.
The inner loop compares that element against the remaining elements.
In the worst case, every element must be compared with almost every other element.
(n(n-1)/2)


Therefore, the time complexity is O(n²).
Auxiliary space: O(1)
The function uses only the loop variables i and j. It does not create another data structure.
"""

# Implementation B — Using a set
def has_duplicate_b(items):
   seen = set()

   for item in items:
       if item in seen:
           return True
       seen.add(item)
   return False


"""
Expected time complexity: O(n)

Reason:
Each element is visited once.
Set membership (item in seen) takes expected O(1) time.
Adding an item to a set also takes expected O(1) time.
Therefore:
O(1) * n = O(n)


Auxiliary space: O(n)
The seen set may store every element when there are no duplicates.
"""

# Implementation C — Sorting first
def has_duplicate_c(items):
   items = sorted(items)
   for i in range(1, len(items)):
       if items[i] == items[i - 1]:
           return True
   return False

   
"""
Worst-case time complexity: O(n log n)

Reason:
sorted(items) sorts the entire list.
Python's sorting algorithm, Timsort, has worst-case O(n log n) time complexity.
The second loop takes O(n) time.
Combining both:
O(n log n)+O(n)= O(n log n)

Auxiliary space: O(n)
sorted() creates a new sorted list rather than sorting the original list in place.
"""


"""Considering the two lists:
1. Distinct integers
numbers = list(range(10000))


2. Duplicate at the beginning
duplicates = [5, 5] + list(range(2, 10000))


Which implementations can return early?
   A can return early when it finds a matching pair.
   B can return early when it encounters an element already in seen.
   C must sort the entire list before it starts checking adjacent elements.


For the second list, A and B can identify the duplicate almost immediately.
C still performs the sorting operation first.


Which does the most work with distinct values?
    Implementation A.
    Because It must compare every possible pair because there are no duplicates to find.


Why is Big O not an exact stopwatch?
    Big O describes how an algorithm's resource requirements (time and space complexities)
    grow as input size increases. It does not tell us the exact execution time.


Actual execution time also depends on hardware, Python implementation, input arrangement, and constant factors.
while Big O is;
    1. Hardware independent
    2. Ignores constants (O(100n) and O(2n) both simplifies to O(n))
    3. And explains the growth curve
"""




# C. Correct the misconception
"""
A student says:
Implementation B is O(1) because set membership is O(1).

This statement confuses the complexity of one operation with the complexity of the entire algorithm.
Considering:
if item in seen:
   return True
seen.add(item)


One set lookup is expected O(1).
However, the function repeats these operations for every element in the input.
For n elements:
O(1)+O(1)+...+O(1)=O(n)

Therefore, the correct expected time complexity of the entire function is O(n).


D. Make an engineering choice
    For millions of records, I would generally choose Implementation B,
    provided the records have suitable hashable values and memory is sufficient.
    Otherwise, it could be dangerous because it must store up to millions of items in system memory simultaneously.

Trade-off:
    Implementation B prioritizes speed at the cost of additional memory.
    If memory is extremely limited, Implementation A uses less auxiliary space but may be prohibitively slow.

    Therefore, if the memory is constrained, and mutating the input in-place is allowed, using items.sort()
    instead of sorted(items) on implementation C would be a better choice
    Another important consideration is that Python sets can experience poor worst-case performance under pathological collision patterns.
"""