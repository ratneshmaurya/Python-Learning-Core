# 👉 Python me set ke saath + operator kaam nahi karta ❌
# 👉 But -, |, &, ^ kaam karte hain ✅

# 🧠 Python me set operators
# 🔹 Example
# a = {1, 2, 3}
# b = {3, 4, 5}
# ✅ Allowed operators
# a - b   # difference
# 👉 Output:{1, 2}

# a | b   # union
# 👉 Output:{1, 2, 3, 4, 5}

# a & b   # intersection
# 👉 Output:{3}

# a ^ b   # symmetric difference (write all things of a and b, except the intersection ones)
# 👉 Output: {1, 2, 4, 5}
# ❌ Not allowed
# a + b
# 👉 Error:TypeError

# ❓ + kyun nahi diya Python ne?
# 👉 Design decision hai in Python
# 👉 Reason:
# + ka meaning ambiguous hota:
# concatenate?
# union?

# 👉 Python ne clear operators diye:
# | → union
# - → difference

# -----------------------------------------------------------------
# 🔥 List vs Set difference
# [1,2] + [3,4]   # works (concatenate)
# {1,2} + {3,4}   # ❌ error

# 👉 Kyunki:
# list = ordered
# set = unordered + unique

# ----------------------------------------------------------------------

# Language difference of python and other language
# 👉 Python me:
# ❌ + nahi
# ✅ |, -, &, ^

# 👉 Other languages:
# ❌ operators nahi
# ✅ functions/methods use hote hain for everything, union ho ya intersection
# ------------------------------------------------------------------------------

essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

# pipe operator is union 
all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")
# output -  All spices: {'cloves', 'cinnamon', 'black pepper', 'ginger', 'cardamom'} , ginger is not printed twice, as it is union

# all_spices = essential_spices + optional_spices  -----> TypeError: unsupported operand type(s) for +: 'set' and 'set'
# print(f"All spices: {all_spices}")

common_spices = essential_spices & optional_spices
print(f"common spices: {common_spices}")
# output - common spices: {'ginger'}

# to remove the things of other from one set, we can use minus
only_in_essential = essential_spices - optional_spices
print(f"Only in essential spices: {only_in_essential}")
# output - Only in essential spices: {'cardamom', 'cinnamon'}


# membership test
# to determine whether a thing is present in that or not, use of in operator
print(f"Is 'cloves' in optional spices? {'cloves' in optional_spices}")

