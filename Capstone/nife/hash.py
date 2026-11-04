def hash_key(keys):
    return sum(ord(char) for char in keys) % 7

# Identify any collisions. Explain why different strings can map to the same index and why a matching index does not prove two keys are equal.
# ANS: different keys can map to the same index bcos they have the same hash value when calculated with the hash function, a matching index doesnt prove two keys are equal bcos, two keys may have the same characters and mean the same thing, therfore having different values also

buckets = [[] for _ in range(7)]     # [ [0], [1], [2], [3], [4], [5], [6] ]

def put(key, value):
    bucket = buckets[hash_key(key)]      # []
    for pair in bucket:
        if pair[0] == key:
            pair[1] = value
            print(buckets)
            return
    bucket.append([key, value])
    print(buckets)

def get(key):
    bucket = buckets[hash_key(key)]      # []
    for pair in bucket:
        if pair[0] == key:
            print(pair[1])
    # print("Not found")
    return None

def delete(key):
    bucket = buckets[hash_key(key)]
    for index, pair in enumerate(bucket):
        if pair[0] == key:
            bucket.pop(index)
    print(buckets)
    return


put("cat", 10)
put("act", 20)
put("cat", 99)
get('cat')
delete('act')
        
