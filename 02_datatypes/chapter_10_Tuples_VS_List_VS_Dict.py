# 11. Kaunsa better hai?


# Situation pe depend karta hai.

# ----------------  LIST use karo when:
# add/remove/update karna ho
# dynamic collection ho

# Example: carts me, as dynamic data hota hai, user add/remove kar sakta hai, toh list use karna chahiye.
# cart = ["shirt", "shoes"]


# ----------------  TUPLE use karo when:
# fixed values ho
# data secure rakhna ho
# coordinates/config etc

# Example: fixed data jise change nahi karna, jaise longitude and latitude, RGB values, month and year, etc.
# point = (10, 20)

# ----------------  DICTIONARY use karo when:
# key-value relation ho
# fast lookup chahiye

# Example:
# student = {
#     "name": "Ratnesh",
#     "marks": 90
# }



# 12. Interview perspective se important line
# Tuple = immutable ordered collection
# List = mutable ordered collection
# Dictionary = mutable key-value collection


#  Important questions ---------------------------------------------------------
# Q. Tuple immutable hai toh andar list modify ho sakti? ---- YES.
t = ([1,2], 5)
t[0].append(3)
print(t)
# Output:
# ([1,2,3], 5)
# Because tuple immutable hai, but uske andar wali list mutable hai.


# Q. Tuple dictionary key kyu ban sakta?
# Because immutable hai and hashable hota hai.
# But only that tuple can be a dictionary key, jisme sirf immutable elements ho, jaise string, number, tuple, etc. 
# Agar tuple ke andar list ya dictionary ho, toh wo dictionary key nahi ban sakta, kyunki wo mutable hota hai.
# {
#    ([1,2], 5): "hello"      --------------> Error: unhashable type: 'list'
# }