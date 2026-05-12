# // example of immutable data type - int
sugar_amount = 2
print(f"Initial sugar: {sugar_amount}")

sugar_amount = 12
print(f"Second Initial sugar: {sugar_amount}")

print(f"ID of 2: {id(2)}")
print(f"ID of 12: {id(12)}")

# Initial sugar: 2
# Second Initial sugar: 12
# ID of 2: 140736390988952
# ID of 12: 140736390989272  (different hence mutable hua as new memory bni)