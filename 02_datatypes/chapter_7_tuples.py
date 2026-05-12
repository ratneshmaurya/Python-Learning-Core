# Tuples means (paranthesis - ())
# Braces means - [] - used for list/arrays
# Curly braces means - {} - used for dictionary


#-------------------------------------- Tuple kya hota hai?
# person = ("Ratnesh", 24, "Delhi")
# Ye ek tuple hai.

# Tuple ko mostly () parentheses me likhte hain.
# Access same list ki tarah:
# print(person[0])   # Ratnesh

# 2. Tuple vs List
# List : fruits = ["apple", "banana"]
# Change kar sakte ho
# fruits[0] = "mango"
# ✅ mutable

# Tuple
# fruits = ("apple", "banana")
# Change nahi kar sakte
# fruits[0] = "mango"
# ❌ Error aayega

# ---------------- uses - thoda faster hota
# memory efficient
# dictionary key ban sakta hai
# fixed data represent karne me useful eg- longitude and latitude, RGB values, month and year, etc.

# ✅ Function multiple values return kare
# def getUser():
#     return ("Ratnesh", 24)
# name, age = getUser()
# Bahut common use hai.



# --------------------------------------------------------------------
# making a tuple
masala_spices = ("cardamom", "cloves", "cinnamon")

# auto destructure it 
(spice1, spice2, spice3) = masala_spices
print(f"Main masala spices: {spice1}, {spice2}, {spice3}")

ginger_ratio, cadramom_ratio = 2, 1
print(f"Ratio is G :{ginger_ratio} and C: {cadramom_ratio}")

# swaping the values, very easily in python
ginger_ratio, cadramom_ratio = cadramom_ratio, ginger_ratio
print(f"Ratio is G :{ginger_ratio} and C: {cadramom_ratio}")

a,b = 1,2;
a,b = b,a;
print(f"swapping normal values as well : {a,b}")


# membership testing ( in used with tuples)
print(f"Is cinnamon in masala spices ? {'cinnamon' in masala_spices}")


# outputs-
# Main masala spices: cardamom, cloves, cinnamon
# Ratio is G :2 and C: 1
# Ratio is G :1 and C: 2
# swapping normal values as well : (2, 1)
# Is cinnamon in masala spices ? True