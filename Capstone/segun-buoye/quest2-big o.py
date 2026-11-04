""" Quest 2 - Big O: Growth, Not Guesswork """

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

"""
Time complexity for A       O(n2)
Space complexity for A      O(1)

Time complexity for B       O(n)
Space complexity for B      O(n)

Time complexity for C       O(nlogn)
Space complexity for C      O(n)

For a list of 10,000 distinct integers, B will be the fastest
"""
