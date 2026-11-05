##########
# QUEST 3 — Hashing and Hash Maps
##########

def hash_key(key): 
  return sum(ord(char) for char in key) % 7 

### A. Calculate: Manually calculate the slot index for 'cat', 'act', 'dog', and 'god'. Show the character code sum and remainder for each.
  # cat = ord('c') + ord('a') + ord('t') = 99 + 97 + 116 = 312; 312 % 7 = 4
  # act = ord('a') + ord('c') + ord('t') = 97 + 99 + 116 = 312; 312 % 7 = 4
  # dog = ord('d') + ord('o') + ord('g') = 100 + 111 + 103 = 314; 314 % 7 = 6
  # god = ord('g') + ord('o') + ord('d') = 103 + 111 + 100 = 314; 314 % 7 = 6

### B. Reason about collisions: Identify any collisions. Explain why different strings can map to the same index and why a matching index does not prove two keys are equal.
  # Collisions:
  # 'cat' and 'act' both map to index 4.
  # 'dog' and 'god' both map to index 6.

  # Different strings can map to the same index due to the modulo operation, which can result in the same remainder for different sums.

  # A matching index does not prove two keys are equal because multiple different strings can have the same hash value, leading to a collision. e.g., 'cat' and 'act' have the same hash value but are different strings.

### C. Implement: Build a seven-slot hash map using separate chaining. Implement put(key, value), get(key), and delete(key). put must update an existing key rather than duplicate it; get must return None for a missing key; delete must remove only the requested key.

# Create seven empty slots
hash_map = [[] for _ in range(7)]

# Add or update a key-value pair
def put(key, value):
  slot = hash_map[hash_key(key)]

  for pair in slot:
    if pair[0] == key:
      pair[1] = value
      return

  slot.append([key, value])

# Retrieve the value associated with a key
def get(key):
  slot = hash_map[hash_key(key)]

  for pair in slot:
    if pair[0] == key:
        return pair[1]

  return None

# Delete only the requested key
def delete(key):
    slot = hash_map[hash_key(key)]

    for i, pair in enumerate(slot):
      if pair[0] == key:
        slot.pop(i)
        return

# Testing the hash map
put("cat", 14)
put("act", 16)
put("dog", 20)

print(get("cat"))  # 14
print(get("act"))  # 16

put("cat", 50)
print(get("cat"))  # 50 (updated)

delete("cat")
print(get("cat"))  # None (deleted)
print(get("act"))  # 16 (still exists)

print(hash_map)


### D. Analyze:  Explain expected time complexity under reasonable hashing assumptions and worst case complexity if all keys land in one bucket. Explain how a larger table may help without guaranteeing O(1)or every operation.

  # Under reasonable hashing assumptions, where keys are uniformly distributed across the hash table, the expected time complexity for `put`, `get`, and `delete` operations is O(1). This is because each operation involves computing the hash value and accessing the corresponding slot, which should take constant time on average.

  # However, in the worst-case scenario where all keys land in one bucket (due to poor hash function or many collisions), the time complexity for these operations can degrade to O(n), where n is the number of keys in that bucket. In this case, we would have to iterate through all the key-value pairs in that single bucket to find, update, or delete a key.

  # A larger table can help reduce the likelihood of collisions by providing more slots for keys to be distributed across. This can improve the average-case performance of the hash map but it also requires more memory and does not guarantee collision-free hashing. The performance will depend on the quality of the hash function and the distribution of keys. 