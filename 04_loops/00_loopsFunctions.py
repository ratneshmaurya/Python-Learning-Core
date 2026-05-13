# Python me loops ke saath kuch bahut important built-in functions use hote hain jo coding ko clean aur powerful bana dete hain.

# Most important:
# range()
# enumerate()
# zip()
# reversed()
# sorted()
# map()
# filter()
# any()
# all()
#  ---------------------------------------------------------------------------

# 1. range()
# Syntax
# range(start, stop, step) 
# Loop ko specific number of times chalane ke liye.

for i in range(5):
    print(i)
# Output: 0 1 2 3 4

# Example
for i in range(1, 10, 2):
    print(i)
# Output: 1 3 5 7 9

# Reverse loop
for i in range(10, 0, -1):
    print(i)

# -----------------------------------------------------------------------------
# 2. enumerate()
# Index + value dono ek saath deta hai.
# Bahut important.

# Without enumerate
fruits = ["apple", "banana"]
for i in range(len(fruits)):
    print(i, fruits[i])

# Messy hota hai, readability kam ho jati hai.

# With enumerate
fruits = ["apple", "banana"]

for index, value in enumerate(fruits):
    print(index, value)

# Output:
# 0 apple
# 1 banana

# Start index bhi de sakte
for i, val in enumerate(fruits, start=1):
    print(i, val)

# Output:
# 1 apple
# 2 banana

#  -------------------------------------------------------------------------------
# 3. zip()
# Multiple lists ko pair karta hai.
# Example

names = ["Ram", "Shyam"]
marks = [90, 80]
for name, mark in zip(names, marks):
    print(name, mark)

# Output:
# Ram 90
# Shyam 80
# Real use case

# Table-like data iterate karna.

# -------------------------------------------------------------
# 4. reversed()
# Reverse order me loop.

nums = [1,2,3]
for n in reversed(nums):
    print(n)

# Output:
# 3 2 1

# -------------------------------------------------------------------
# 5. sorted()
# Loop se pehle sorted iteration.

nums = [4,1,3]
for n in sorted(nums):
    print(n)

# Output:
# 1 3 4

# Reverse sorting
sorted(nums, reverse=True)

# ----------------------------------------------------------------------
# 6. map()
# Har element pe function apply karta hai.
# Example

nums = [1,2,3]
squares = map(lambda x: x*x, nums)
print(list(squares))
# Output:
# [1, 4, 9]

# Common input use
nums = list(map(int, input().split()))

# --------------------------------------------------------------------------
# 7. filter()
# Condition ke basis pe items select karta.

nums = [1,2,3,4]
evens = filter(lambda x: x % 2 == 0, nums)
print(list(evens))

# Output:
# [2, 4]


# -=----------------------------------------------------------------
# 8. any()
# Koi ek bhi True ho toh True.

# nums = [0,0,5]
# print(any(nums))

# Output:
# True
# Because 5 truthy hai.


# ------------------------------------------------------------------------
# 9. all()
# Sab True hone chahiye.

nums = [1,2,3]
print(all(nums))

# Output:
# True


# -----------------------------------------------------------------------------
# 10. len()
# Loop count ke liye.

# names = ["a", "b"]

# print(len(names))


# ----------------------------------------------------------------------

# 11. items() for dictionary
# Dictionary loop me very important.

student = {
    "name": "Ratnesh",
    "age": 24
}

for key, value in student.items():
    print(key, value)


# ----------------------------------------------------------------
# 12. keys() and values()
# keys
for k in student.keys():
    print(k)
# values
for v in student.values():
    print(v)



# ----------------------------------------------------------------
# 13. List comprehension (VERY IMPORTANT)
# Short loop syntax.

# Normal
# squares = []

for i in range(5):
    squares.append(i*i)

# Comprehension
squares = [i*i for i in range(5)]

# Condition inside comprehension
evens = [x for x in range(10) if x % 2 == 0]



# ------------------------- IMPORTANT SUMMARY -------------------------
# 14. Quick interview summary
# Function	Purpose
# range()	generate sequence
# enumerate()	index + value
# zip()	combine iterables
# reversed()	reverse iteration
# sorted()	sorted iteration
# map()	transform items
# filter()	filter items
# any()	at least one True
# all()	all True
# items()	dict key-value loop