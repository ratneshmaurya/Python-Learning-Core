import sys
from fractions import Fraction
from decimal import Decimal

ideal_temp = 95.5
current_temp = 95.49
current_temp_new = 95.499999999

print(f"Ideal temp { ideal_temp }")
print(f"Current temp { current_temp }")
print(f"Difference temp { ideal_temp - current_temp }")
print(f"Difference temp new { ideal_temp - current_temp_new }")
print(sys.float_info)


# Issue floation precision error in every language (c++, java, python etc)
# 🧠 1. Computer number ko kaise store karta hai?
# 👉 Computer sirf 0 aur 1 (binary) samajhta hai

# 🔹 Integer case (easy)
# 5 (decimal) = 101 (binary)

# 👉 Exact store ho jata hai ✅
# 👉 No issue

# 🔴 Problem start hoti hai → decimal (float) me
# Example: 0.1

# 👉 Decimal me:
# 0.1

# 👉 Binary me convert karo:
# 0.0001100110011001100110011... (infinite)
# 👉 😵 Ye kabhi khatam hi nahi hota

# ⚠️ Important concept
# 👉 Computer ke paas limited memory hoti hai
# 👉 Wo infinite digits store nahi kar sakta

# 👉 Isliye:
# ➡️ cut / round kar deta hai

# 0.0001100110011001 (approx)

# 👉 Yahi error ka source hai

# 🧪 Ab tumhara example samjho
# 95.499999999

# 👉 Ye binary me exact represent nahi hota
# 👉 To computer store karta hai approx value

# 👉 Fir subtraction:
# 95.5 - 95.499999999

# 👉 Actual me ho raha hai:
# approx1 - approx2

# 👉 Result:
# thoda off (weird number)

# hence we use precisions in java, c++, pythons
# in java we use - BigDecimals
# in c++ - we use setPrecision
# in python we use Decimal("0.1");


# Why doesn't 0.1+0.2-0.3 equal 0.0 ?
# This has to do with floating point accuracy and computer's abilities to represent numbers in memory. 
# For a full breakdown, check out: https://docs.python.org/2/tutorial/floatingpoint.html



# In Python 3, what is the output of 1/2 ? === 0.5
# in Python 3, the division of integers yields a float result through true division. 
# When you divide 1 by 2, the result is not zero, but instead is a fractional value. 
# This highlights how Python handles division differently than some other programming 
# languages that might perform integer division by default.