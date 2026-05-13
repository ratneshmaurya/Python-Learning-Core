
# zip in python is a built-in function that allows you to combine two or more iterables (like lists, tuples, etc.) 
# into a single iterable of tuples. Each tuple contains one element from each of the input iterables, 
# paired together based on their positions.

names = ["Hitesh", "Meera", "Sam", "Ali"]
bills = [50, 70, 100, 55]

for name, amount in zip(names, bills):
    print(f"{name} paid {amount} rupees")

# output:
# Hitesh paid 50 rupees
# Meera paid 70 rupees
# Sam paid 100 rupees
# Ali paid 55 rupees