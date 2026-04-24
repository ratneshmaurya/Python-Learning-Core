# 🧠 Mutable vs Immutable (simple meaning)
# 🔹 Immutable
# 👉 Change nahi kar sakte (in-place)
# 👉 Value same rahegi, nayi value banani padegi

# 🔹 Mutable
# 👉 Change kar sakte ho (in-place)
# 👉 Same object modify hota hai

# 🔥 Visual samajh lo
# ❌ Immutable
# x = "hello"
# x[0] = "H"   # ❌ error
# 👉 Change allowed nahi

# ✅ Mutable
# lst = [1, 2, 3]
# lst[0] = 10
# print(lst)
# 👉 Output:
# [10, 2, 3]
# 👉 Same list modify hui

# ⚔️ Python me kaun kya hai?
# 🔴 Immutable types
# 👉 Ye change nahi hote:
# int
# float
# bool
# str
# tuple
# bytes

# 🟢 Mutable types
# 👉 Ye change ho sakte hain:
# list
# set
# dict
# bytearray


# 🧪 Important example (tricky)
# 🔹 String
# name = "ram"
# name = "Ram"
# 👉 Tumhe lagta hai change hua
# 👉 But actually:
# ➡️ new string bani

# 🔹 List
# a = [1,2]
# b = a
# a.append(3)
# print(b)
# 👉 Output:
# [1, 2, 3]
# 👉 Same object modify hua

# 🧠 Memory concept (important)
# Immutable:
# x = 10
# x = 20
# 👉 10 delete nahi hua
# 👉 new memory create hui

# Mutable:
# list modify hoti hai same memory me
# 👉 no new object (usually)