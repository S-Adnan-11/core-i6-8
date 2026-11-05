def hash_key(key): 
    return sum(ord(char) for char in key) % 7


class HashMap:
    def __init__(self):
        self.entries = [()] * 7 

    def put(self, key, value):
        hash_index = hash_key(key)
        self.entries[hash_index] = (key, value)

    def get(self, key):
        hash_index = hash_key(key)
        kv_pair = self.entries[hash_index]
        if not kv_pair or kv_pair[0] != key:
            return None 
        return kv_pair[1]

    def delete(self, key):
        hash_index = hash_key(key)
        kv_pair = self.entries[hash_index]
        if kv_pair[0] == key:              
            self.entries.pop(hash_index)
            return f"Key has been deleted"
        else:
            return f"Key can't be deleted"
        


hash_map = HashMap()
hash_map.put('cat', 1)
hash_map.put('dog', 2)

print(hash_map.get('cat'))
print(hash_map.get('dog'))
print(hash_map.delete('cat'))
             
print(hash_map.get('cat'))