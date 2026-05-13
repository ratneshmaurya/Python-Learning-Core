# Enumerate in Python is a built-in function that allows you to loop over an iterable (like a list, tuple, etc.) 
# and have an automatic counter. (by default start from 0) It returns an enumerate object, which is 
# an iterator that produces pairs of index and value from the iterable.

menu = ["Green", "Lemon", "Spiced", "Mint"]

for idx, item in enumerate(menu, start=1):
    print(f"{idx} : {item} chai")

# output :
# 1 : Green chai
# 2 : Lemon chai
# 3 : Spiced chai
# 4 : Mint chai