
# operator overloading means, jo normal kaam hai operator ka, like adding number things
# same operator (+, -, , etc.) ko different types ke objects pe alag tarike se behave karwana
# this is in every language, by default written rhta. we can change functionlaity if we want

# 👉 Socho:
# “+” ka matlab:
# numbers → add
# strings → join
# lists → merge

# 👉 Matlab: Same symbol, different meaning
# ye sb define hota hai in each class of python, i.e adding, substraction and all ke classes me define rhta ki kaise handle kre
# and uss definition ko hi operator overloading khte hai

# 👉 Example: [1, 2] + [3, 4]
# 👉 Internally: [1,2].__add__([3,4])
# Hence we can change the functionality of + function, inside __add__ function of Add class in python, 
# if want that + operator should do something else other than adding two list element
# 👉 Python me internally special methods hote hain:
# for + python have this function __add__
# for - python have this function __sub__

# a + b
# ↓
# a.__add__(b)
# ↓
# type-specific implementation
# ↓
# new object return

#-------------------------------------------------------------------------------------
# operations on list of strings
base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]

# so instead of doing it by using append or extends functions, we are doing by operator overloading
full_liquid_mix = base_liquid + extra_flavor
print(f"Liquid mix: {full_liquid_mix}")
#  output - Liquid mix: ['water', 'milk', 'ginger']

strong_brew = ["black tea"] * 3
print(f"String brew: {strong_brew}")
# output - String brew: ['black tea', 'black tea', 'black tea']

strong_brew = ["black tea", "water"] * 3
print(f"String brew: {strong_brew}")
# output - String brew: ['black tea', 'water', 'black tea', 'water', 'black tea', 'water']

# -----------------------------------------------------------------------------------------
# 👉 bytearray = mutable sequence of bytes (0–255 values)
# ➡️ binary data ka list jaisa version, jisko change kar sakte ho
# 👉 Har character → number (ASCII)

raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(f"Bytes: {raw_spice_data}")