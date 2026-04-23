# Tuples (paranthesis - ())
# Braces - []
# Curly braces - {}

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