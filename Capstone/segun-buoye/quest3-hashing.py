""" Quest 3 - Hashing and Hash Maps """

def hash_key(key):
    return sum(ord(char) for char in key) % 7

hash_map = [[] for _ in range(7)]

def put(key, value):
    slot = hash_map[hash_key(key)]

    for pair in slot:
        if pair[0]== key:
            pair[1] == value
            return
    slot.append([key, value])
    print(hash_map)

def get(key):
    slot = hash_map[hash_key(key)]

    for pair in slot:
        if pair[0]== key:
            return pair[1]
    print("Not found")
    return None

def delete(key):
    slot = hash_map[hash_key(key)]

    for i, pair in enumerate(slot):
        if pair[0] == key:
            slot.pop(i)
    print(hash_map)

#for testing 

put("cat", 14)
put("act", 16)
put("big", 13)
print(get("big"))
delete("big")

