# in list the index is default, i.e 0, then 1 then 2
# but in dictionary, we can choose our indexing, we can name them i.e values can we pointed/accessed using some other names

# dictionary me key-value pair hota hai, jisme key unique hota hai, aur uske corresponding value hoti hai.
# dictionary me order maintain nahi hota, matlab jab bhi print karoge, order change ho sakta hai, kyunki wo internally hash table use karta hai.
# dictionary me keys immutable hoti hain, matlab string, number, tuple, etc. lekin list nahi le sakta kyunki wo mutable hoti hai.
# dictionary me values mutable ya immutable dono ho sakti hain, matlab list, tuple, string, number, etc. sab kuch ho sakta hai.

#  why keys are immutable in dictionary ?
# Python dictionary internally hash table use karti hai.
# Aur hash table properly kaam kare, isliye:
# Dictionary keys immutable (hashable) honi chahiye.

# ----------------------- Internal working of dictionary:---------------- Similar to hashmaps
# Suppose

data = {
    "name": "Ratnesh"
}
# Python "name" ko directly store nahi karta.
# Wo internally: hash("name")
# calculate karta hai.

# Example:
# hash("name") -> 12345
# Fir us hash ke basis pe memory location decide hoti hai.
# Isi wajah se dictionary lookup bahut fast hota hai.
# And hence hum mutable cheej ko key nhi bnate, i.e list ko nhi, becoz usme hum append ya remove krenge toh hash change ho jaaega.



# ------------------------------- PRACTICALS-------------------

chai_order = dict(type="Masala Chai", size="Large", sugar=2)
print(f"Chai order: {chai_order}")
# output - Chai order: {'type': 'Masala Chai', 'size': 'Large', 'sugar': 2}

# ----------------------------------------another way of defining the dictionary
chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f"Recipe base: {chai_recipe['base']}")
# output - Recipe base: black tea

print(f"Recipe: {chai_recipe}")
# output - Recipe: {'base': 'black tea', 'liquid': 'milk'}

# just need the key to remove that entry data
del chai_recipe["liquid"]
print(f"Recipe: {chai_recipe}")
# output - Recipe: {'base': 'black tea'}


# membership test
print(f"Is sugar in the order? {'sugar' in chai_order}")


# ------------------------------- .keys(), .values(), .items() and .popitem(), .update() -------------------------------
chai_order = {"type": "Ginger Chai", "size": "Medium", 1: "sugar"}
print(f"Order details (keys): {chai_order.keys()}")
print(f"Order details (values): {chai_order.values()}")
print(f"Order details (items): {chai_order.items()}")

last_item = chai_order.popitem()
print(f"Removed last item: {last_item}")
# output- Removed last item: ('sugar', 1)

extra_spices = {"cardamom": "crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices)
print(f"Updated chai recipe: {chai_recipe}")
# output - Updated chai recipe: {'base': 'black tea', 'cardamom': 'crushed', 'ginger': 'sliced'}

#  ------------------------------.get() method-------------------------------
# Generally, if the key we look for is not there in the dictionary, it will raise a KeyError. 
# But with .get() method, we can provide a default value to return if the key is not found, instead of raising an error.
customer_note = chai_order.get("newNote", "NO Note")
print(f"customer_note is: {customer_note}")
# output - customer_note is: NO Note

#  but if the key is present, it will return the corresponding value.
customer_note = chai_order.get("size", "NO Note")
print(f"customer_note is: {customer_note}")
# output - customer_note is: Medium