import random
import time
def hash_key(key):
    return sum(ord(char) for char in key) % 7

#Question A
# test="cat"
# test_total=sum([ord(char) for char in test])
# print(f"{test} sum: {test_total} | Remainder: {test_total%7}")
# test="act"
# test_total=sum([ord(char) for char in test])
# print(f"{test} sum: {test_total} | Remainder: {test_total%7}")
# test="dog"
# test_total=sum([ord(char) for char in test])
# print(f"{test} sum: {test_total} | Remainder: {test_total%7}")
# test="god"
# test_total=sum([ord(char) for char in test])
# print(f"{test} sum: {test_total} | Remainder: {test_total%7}")
"""
Question B
Name collisions occurs when two words are anagrams hence
their sum of ASCII  values becomes same. But the two words themselves are not same
"""

#Question C

def put(hashmap,key,value):
    index=hash_key(key)
    found=False
    for i in range(len(hashmap[index])):
        if hashmap[index][i][0]==key:
            found=True
            hashmap[index][i]=(key,value)
            break
    if not found:
        hashmap[index].append((key,value))
    

def get(hashmap,key):
    index=hash_key(key)
    for i in hashmap[index]:
        if i[0]==key:
            return i[1]
    return None
    

def delete(hashmap,key):
    index=hash_key(key)
    for i in range(len(hashmap[index])):
        if hashmap[index][i][0]==key:
            del hashmap[index][i]
            break
        

hash=[[] for _ in range(7)]
# print(hash)
put(hash,"cat",3)
put(hash,"act",5)
put(hash,"act",6)
put(hash,"dog",7)
put(hash,"ndukc",8)
delete(hash,"cat")
# print(hash)
"""
Question D
The longer the length of keys the longer time it takes to harsh it
This is because harshing the key involves running a for loop and add each character up

The larger the bucket the higher the chances of have reduced collisions.
Now there's bucket space . 
Though anagrams and words that have same some of ascii values will always be in same bucket
but using an example below
assume sum values of two words are 7 and 14.
using 7 slot  will result to remainder 0 for both words
which implies they would be in same bucket even though they are not anagrams
but using slot 10 will result to 7 and 4. now they have been split into two different buckets.
So the higher the slot the better. 
"""


#Dictionary Experiment to proof it is not neccessary O(n)

# def generate_word(n,num_of_words):
#     letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#     letters=letters+[k.upper() for k in letters]
#     word=""
#     result=[]
#     # for i in range(num_of_words):
#     #     word=""
#     for i in range(n):
#         word+=letters[random.randint(0,len(letters)-1)]
#     result.append(word)
#     for i in range(num_of_words):
#         index=random.randint(0,len(letters)-2)
#         word=word[:index]+word[index+1:]
#         result.append(word)
        
    
#     return result

# def dict_test(words):
#     test={}
#     for i in words:
#         if i not in test:
#             test[i]=1
#         else:
#             test[i]+=1
    
# word1=["yes","no","good","yecccccccs","nduka","godstime","oweniwe","ayomide","dorcase","bishop"]
# word1=word1+word1+word1+word1
# start=time.time()
# word2=generate_word(200000000,39)
# end=time.time()
# print("Time to Generate Word: ",end-start)

# start=time.time()
# dict_test(word1)
# end=time.time()
# print("Time taken for short words: ",end-start)

# start=time.time()
# dict_test(word2)
# end=time.time()
# print("Time taken for long words: ",end-start)

