
# A. Calculate the slot index
"""Given:
def hash_key(key):
return sum(ord(char) for char in key) % 7"""

#Calculating each string.

"""1. 'cat'
c = 99
a = 97
t = 116
99 + 97 + 116 = 312
312 % 7 = 4
Slot 4


2. 'act'
a = 97
c = 99
t = 116
97 + 99 + 116 = 312
312 % 7 = 4
Slot 4


3. 'dog'
d = 100
o = 111
g = 103
100 + 111 + 103 = 314
314 % 7 = 6
Slot 6


4. 'god'
g = 103
o = 111
d = 100


103 + 111 + 100 = 314


314 % 7 = 6
Slot 6
"""

# B. Reason about collisions.
"""
    A collision occurs when two different keys produce the same hash index.
    We have two collisions:
    cat and act both map to slot 4.
    dog and god both map to slot 6.
"""

# Why do collisions happen?
"""
    This happens because our hash function adds character codes without considering character positions.
    Therefore, rearranging the same characters produces the same total.
"""
# For example:
# cat = 99 + 97 + 116 = 312
# act = 97 + 99 + 116 = 312
# Both produce the same index.


# Why doesn't a matching index prove that two keys are equal?

"""
    Because the hash function maps potentially many different keys into only seven available slots.
    The index identifies where to search, not which exact key is stored there.
    We must still compare the original keys using equality (==)."""


# C. Implement a seven-slot hash map.

def hash_key(key):
   return sum(ord(char) for char in key) % 7

class HashMap:
   def __init__(self):
       self.table = [[] for _ in range(7)]


   def put(self, key, value):
       index = hash_key(key)


       bucket = self.table[index]
       for pair in bucket:
           if pair[0] == key:
               pair[1] = value
               return            
       bucket.append([key, value])

   def get(self, key):
       index = hash_key(key)
       bucket = self.table[index]

       for pair in bucket:
           if pair[0] == key:
               return pair[1]
       return None
   def  delete(self, key):
       index = hash_key(key)
       bucket = self.table[index]

       for i in range(len(bucket)):
           if bucket[i][0] == key:
               del bucket[i]
               return True
       return False
  


my_map = HashMap()

#  # Normal insertions
my_map.put("cat", 100)
my_map.put("act", 200)
my_map.put("dog", 300)
my_map.put("god", 400)


print(my_map.get("cat"))  # 100
print(my_map.get("act"))  # 200
print(my_map.get("dog"))  # 300
print(my_map.get("god"))  # 400


#  # Update existing key
#  my_map.put("cat", 500)


#  print(my_map.get("cat"))  # 500


#  # Delete one colliding key
#  print(my_map.delete("cat"))  # True


#  print(my_map.get("cat"))  # None
#  print(my_map.get("act"))  # 200

#  # Missing key
#  print(my_map.get("bird"))  # None
#  print(my_map.delete("bird"))  #False

# Important edge case:
# Deleting cat must not delete act, even though both keys occupy slot 4.


# D. Hash map analysis:
"""Expected performance
With a well-distributed hash function and a dynamically resized table:
    put() — expected O(1).
    get() — expected O(1).
    delete() — expected O(1).

However, our implementation has a fixed seven-slot table.
As more keys are inserted, buckets become longer. With seven fixed buckets,
the expected bucket length grows proportionally to the number of stored keys.
Therefore, for this exact implementation, operations are O(n)
as the number of keys grows, assuming the seven buckets remain fixed."""


# Worst-case performance
"""Suppose every key lands in the same bucket.
The bucket could look like this:
[
   ["cat", 100],
   ["act", 200],
   ["dog", 300],
   ["god", 400]
]

The time complexity becomes O(n) for lookup, insertion, and deletion."""

# How does a larger table help?
"""
    A larger table provides more available buckets, potentially distributing
    keys more evenly and reducing collisions.
    However, a larger table does not guarantee O(1) operations.
    A poor hash function can still send many keys into the same bucket."""