
# Concepts I found most intriguing:
"""Decorators and hashmaps."""

# My first incorrect assumption:
"""
    Initially, I assumed that if two keys produced the same hash index, they were the same key.
    I thought the hash index was enough to identify the stored value."""

# Evidence that changed my mind:
"""
    When I calculated the hash values of cat and act, I discovered
    that both produced index 4, even though they were different strings.
    This helped me understand that a hash function only determines
    where a key should be stored. The actual key must still be compared to
    distinguish between different entries."""

# Edge case:
# my_map = HashMap()

#  my_map.put("cat", 100)
#  my_map.put("act", 200)

#  print(my_map.get("cat"))
#  print(my_map.get("act"))
# Predicted output:
# 100
# 200

"""Both keys occupy the same bucket, but they must return different values."""

# Test to prevent the same mistake:
"""
    I would always test two different keys that produce the same hash
    index and verify that retrieving or deleting one does not affect the other."""


# Why my solution is correct:
"""My implementation handles collisions using separate
chaining and compares the actual keys before updating, retrieving, or deleting values."""