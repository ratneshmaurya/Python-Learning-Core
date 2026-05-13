# 👉 Different brackets = different data types ✅

# ------------------------------------ Square brackets [] → List ------------------------------------
# 🔹 1. Square brackets [] → List
# a = [1, 2, 3]
# 👉 Mutable
# 👉 Ordered
# 👉 Duplicate allowed
# ------------------------------------Parentheses () → Tuple -----------------------------------
# 🔹 2. Parentheses () → Tuple
# t = (1, 2, 3)
# 👉 Immutable
# 👉 Ordered
# eg -> t = (1, 2, 3)
# t[0] = 10   # ❌ error
# 👉 Error: TypeError: 'tuple' object does not support item assignment

# 👉 Tuple immutable hai
# 👉 But agar uske andar mutable object ho, wo change ho sakta hai

# 🔧 Example
# t = ([1, 2], 3)
# t[0].append(99)
# print(t)
# 👉 Output: ([1, 2, 99], 3)

# 👉 😵 Yeh kaise hua?
# 👉 Kyunki:
# tuple change nahi hua
# but list inside tuple change ho gayi

# --------------------------------- Curly braces {} → Set / Dictionary -----------------------------------------
# 🔹 3. Curly braces {} → Set / Dictionary
# 👉 Set
# s = {1, 2, 3}
# 👉 Unordered
# 👉 Unique values
# ------------- Duplicate automatically remove
# nums = {1, 2, 2, 3}
# print(nums)
# Output:
# {1, 2, 3}

# 👉 Dictionary eg-> d = {"name": "Ram", "age": 20} i.e Key-value pairs
# ⚠️ Important confusion
# 👉 {} empty likhoge: x = {}
# 👉 Ye set nahi, dictionary hai ❗

# ----------------- Empty set kaise banate hain?
# s = set()

# --------------------------SUMMARY-----------------------------------------------------------
# Bracket	Type	Example
# []	List	[1,2,3]
# ()	Tuple	(1,2,3)
# {}	Dict / Set	{1,2} / {"a":1}

# 💡 Easy trick yaad rakhne ka
# 👉 [] → list (shopping list 📋)
# 👉 () → tuple (fixed group 🔒)
# 👉 {} → set/dict (unique / mapping 🧠)