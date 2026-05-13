flavours = ["Ginger", "Out of Stock", "Lemon", "Discontinued", "Tulsi"]


for flavour in flavours:
    if flavour == "Out of Stock":
        continue
    if flavour == "Discontinued":
        print(f"{flavour} item found")
        break
    print(f"{flavour} item found")
    
print(f"Out side of loop")

# output :
# Ginger item found
# Lemon item found
# Discontinued item found
# Out side of loop