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
has_duplicate_a 
time_complexity - O(n^2) - Nested loop
space_complexity - O(1) = no extra space

has_duplicate_b 
time_complexity = O(n) - Single iteration 
space_complexity = O(n) - set initalization of n elements in items

has_duplicate_c
time_complexity = O(nlogn) - sort operation takes higher precednce over the iteration
space_complexity = O(n) - new items placeholder storing sorted numbers

"""
