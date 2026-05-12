# Ye f ka matlab hota hai:
# f-string (formatted string)

# Python me variables ko string ke andar directly inject karne ke liye use hota hai.

# example code:

for token in range(1, 11):
    print(f"Serving chai to Token #{token}")

# Without f
# Agar f hata do:
# print("Serving chai to Token #{token}")
# Output:
# Serving chai to Token #{token}
# Python isko normal string samjhega.

# With f
print(f"Serving chai to Token #{token}")

# Output:
# Serving chai to Token #1
# Serving chai to Token #2

# -------------------------------- write once and use many times - 
product = "iPhone"
price = 80000
print(f"{product} costs ₹{price}")



# -------------------------------- Old ways before f-string
# 1st way => String concatenation
print("Hello " + name)
# Messy ho jata.

# 2nd way => .format()
print("Hello {}".format(name))

# Why f-string best?
# ✅ readable
# ✅ clean
# ✅ fast
# ✅ modern Python way