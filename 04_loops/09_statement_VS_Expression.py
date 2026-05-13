# Programming me:
# Expression → value produce karta hai
# Statement → action perform karta hai
# Ye core programming concept hai.


# ------------------------------------------------------  Expression kya hota hai?
# Anything that evaluates to a value.
# Matlab final me ek value milti hai.

# Examples
# 5 + 3
# Ye evaluate hoga:8
# So this is an expression.

# More examples
# 10
# name
# a > b
# "Hello"
# len([1,2,3])

# Sab value return karte hain.
# So sab expressions hain.

# ------------------------------------------------------ Statement kya hota hai?
# Instruction/action that Python execute karta hai.
# Ye zaruri nahi value return kare.

# Examples
# if x > 5:
#     print(x)
# Ye action hai.

# for i in range(5):
#     print(i)
# Loop statement.


# ------------------------- PRINTING CASE -------------------------
# Expression ko print kar sakte
# print(5 + 3)
# Because expression value deta hai.

# Statement ko print nahi kar sakte
# print(if x > 5)
# ❌ Invalid syntax
# Because if statement hai, value nahi.

# ------------------------- ASSIGNEMENT CASE -------------------------
# Assignment interesting case
# x = 10
# Ye statement hai.

# But:
# 10
# expression hai.

# ----------------------------- IF VS TERNARY EXPRESSION -----------------------------

# This is Statement
# if age > 18:
#     result = "Adult"
# else:
#     result = "Minor"


# But this is Expression
# result = "Adult" if age > 18 else "Minor"


# ------------------------------- Function calls -------------------------------
# Function call expression hai?
# YES.
# Python me function call generally expression hota hai because:
# Har function call ek value evaluate karta hai.
# Even agar function explicitly kuch return na kare tab bhi.

# len([1,2,3])
# returns value.

# print() ?
# Even print() bhi technically expression hai
# print("Hello")

# Ye internally return karta:
# None

# Matlab value still return ho rahi hai.
# Bas mostly side effect ke liye use hota.

# ---------------------------------- Lmabda functions ----------------------------------
# Lambda always expression hota
# lambda x: x * 2

# Expression.