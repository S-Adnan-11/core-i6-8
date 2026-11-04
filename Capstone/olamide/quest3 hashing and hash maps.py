def hash_key(key):
    return sum(ord(char) for char in key) % 7

"""A. Calculate (5 marks): 
Manually calculate the slot index for 'cat', 'act', 'dog', and 'god'. 
Show the character-code sum and remainder for each."""

"""
cat = 99 + 97 + 116 = 312
312 % 7 = 4

act = 97 + 99 + 116 = 312
312 % 7 = 4

dog = 100 + 111 + 103 = 314
314 & 7 = 6

god = 103 + 111 + 100 = 314
314 & 7 = 6
"""

"""B. Reason about collisions (5 marks): 
Identify any collisions. 
Explain why different strings can map to the same index 
and why a matching index does not prove two keys are equal."""
"""
cat and act collide
dog and god collide

There is no perfect hashing function.
There is always a limit to the maximum number a hashing function
can return but there is no limit to the variety of input that can exist.
"""

"""C. Implement (10 marks): 
Build a seven-slot hash map using separate chaining. 
Implement put(key, value), get(key), and delete(key). 
put must update an existing key rather than duplicate it; 
get must return None for a missing key; 
delete must remove only the requested key."""

class sevenSlotHashMap:
    def __init__(self):
        self._arr = [[] for _ in range(7)]
        
    def hash_key(key: str) -> int:
        return sum(ord(char) for char in key) % 7

    def put(self, key: str, value):
        idx = sevenSlotHashMap.hash_key(key)
        for i, kvPair in enumerate(self._arr[idx]):
            if kvPair[0] == key:
                self._arr[idx][i] = (key, value)
                return
        self._arr[idx].append((key, value))

    def get(self, key: str):
        idx = sevenSlotHashMap.hash_key(key)
        for kvPair in self._arr[idx]:
            if kvPair[0] == key:
                return kvPair[1]
        return None

    def delete(self, key):
        idx = sevenSlotHashMap.hash_key(key)
        for i, kvPair in enumerate(self._arr[idx]):
            if kvPair[0] == key:
                del self._arr[idx][i]
                return True
        return False

if __name__ == "__main__":
    sshm = sevenSlotHashMap()
    sshm.put("cat", 3)
    sshm.put("act", 4)
    sshm.put("dog", 7)
    sshm.put("god", 0)
    # sshm.put("cat", 6)
    # print(sshm.get("cat"))
    # sshm.delete("act")
    print(*sshm._arr, sep="\n")

"""D. Analyze (5 marks): 
Explain expected time complexity under reasonable hashing assumptions 
and worst-case complexity if all keys land in one bucket. 
Explain how a larger table may help without guaranteeing O(1) for every operation."""

"""
Under reasonable assumptions the time complexity is O(1) for put, get and delete.
Worst case scenario it is O(n) if all keys land on the same bucket 
it is not different from an array.

The larger the table and the more distribution in the hashing function
the more the time complexity tends toward O(1).
"""
