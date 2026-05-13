
# Python me := ko bolte hain: Walrus Operator
# Official name: Assignment Expression
# Ye Python 3.8 me introduce hua tha.

# Ye karta kya hai?
# Ek hi line me: value assign bhi karta aur use bhi karta

# Normal way
name = input("Enter name: ")
if name:
    print(name)

# Walrus operator way
if name := input("Enter name: "):
    print(name)

# Yaha:
# name := input(...)
# input ko name me store bhi kar raha
# aur condition me use bhi kar raha

# Why called walrus?
# Because: :=
# thoda walrus face jaisa dikhta 😄 (wild sea mammal with two outer long teeth)

# ------------------------------ Assignment statement vs Assignment expression ------------------------------
# = assignment statement hai
x = 5

# := assignment expression hai
print(x := 5)
Output:5

# Why normal = not allowed inside if?
# This invalid hai:
# if x = 5:
# ❌ SyntaxError
# Because = statement hai, expression nahi.

# Walrus solve karta:
if (x := 5):  # as this is assignment expression not statement
    print(x)

# ------------------------------------------------------------- Another example ----------------
# available_sizes = ["small", "medium", "large"]
# if (requested_size := input("Enter your chai cup size: ")) in available_sizes:
#     print(f"Serving {requested_size} chai")
# else:
#     print(f"Size is unavailable - {requested_size}")


# Another example ---------------- with while loop
flavors = ["masala", "ginger", "lemon", "mint"]
print("Available flavors: ", flavors)

while (flavor := input("Choose your flavor: ")) not in flavors:
    print(f"Sorry, {flavor} is not available")

print(f"You choose {flavor} chai")