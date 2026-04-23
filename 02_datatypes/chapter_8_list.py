
# list - same as array (list is mutable)
ingredients = ["water", "milk", "black tea"]
ingredients.append("sugar")
print(f"Ingredients are: {ingredients}")
ingredients.remove("water")
print(f"Ingredients are: {ingredients}")

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

# adding the extra elements of other array to another one
chai_ingredients.extend(spice_options)
print(f"chai: {chai_ingredients}")

# adding any element at any specific positions
chai_ingredients.insert(2, "black tea")
print(f"chai: {chai_ingredients}")

# pop remove it from list and give us that element value as well
last_added = chai_ingredients.pop()
print(f"{last_added}")
print(f"chai: {chai_ingredients}")

# to revers it directly (list is mutable)
chai_ingredients.reverse()
print(f"chai: {chai_ingredients}")
chai_ingredients.sort()
print(f"chai: {chai_ingredients}")

sugar_levels = [1, 2, 3, 4, 5]
print(f"Maximum sugar level: {max(sugar_levels)}")
print(f"Minimum sugar level: {min(sugar_levels)}")
