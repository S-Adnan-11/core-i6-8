"""Each function checks whether a list contains a duplicate:"""
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

"""A. Analyze (9 marks): 
For each implementation, 
state the worst-case or expected time complexity as appropriate, 
plus auxiliary space complexity. 
Point to the operations that create that cost."""

"""
has_duplicate_a:
Worst case: no duplicate.
Time complexity: O(n^2)
Space complexity: O(1)
Costly operation(s): The nested for loops that loop over the same list.
for i in range(len(items)):
    for j in range(i + 1, len(items)):
    
has_duplicate_b:
Worst case: no duplicate.
Time complexity: O(n)
Space complexity: O(n)
Costly operation(s): Saving every value into the seen set.
seen.add(item)

has_duplicate_c:
Worst case: unsorted items and no duplicates
Time complexity: O(nlog(n))
Space complexity: O(1)
Costly operation(s): sorting the items list
items = sorted(items)
"""

"""B. Predict before running (5 marks): 
Compare a list of 10,000 distinct integers with 
a list whose first two values are equal. 
Which implementations can return early? 
Which is likely to do the most work on distinct values? 
Explain why Big O is not an exact stopwatch."""

"""
                |10,000 distinct Integer            |first two are equal        |
has_duplicate_a |10,000^2 = 100,000,000 comparisons | 1 comparison              |
has_duplicate_b |10,000 comparisons                 | 2 comparisons             |
has_duplicate_c |10,000 comparisons after sorting   | 1 comparison after sorting| 
"""

"""C. Correct the misconception (5 marks): 
A student says, “Implementation B is O(1) because set membership is O(1).” 
Explain the difference between the expected cost of one set lookup 
and the cost of processing n items."""

"""
We are not doing one set look up we are doing n set look ups.
If we do a O(1) process n times it becomes O(n).
"""

"""D. Make an engineering choice (6 marks): 
Choose an implementation for millions of records. 
Discuss speed, memory, sorting/input mutation, 
and what collision-heavy hashing could mean. 
A strong answer names a trade-off."""

"""
I would recommend has_duplicate_c the records are to be check for duplicates
more than once and has_duplicate_b for just one check.

has_duplicate_a would have to do a quadrillion comparisons
if the millions of records are distinct.

has_duplicate_b would have to use approximately 1 million * record size
worth of extra space. Plus the set would have to be managed properly in
order for every look up to be O(1), this is hard to do for an approximately
1 million length set. For a single look up has_duplicate_b is best since
the memory can be freed after but for a continuous set up it is not the
best choice.

has_duplicate_c only needs to sort the list once. 
After that every run can be O(n) the same as has_duplicate_b without the
extra memory. For a continuous set up this is best but for a single look up
has_duplicate_b is best.
"""
