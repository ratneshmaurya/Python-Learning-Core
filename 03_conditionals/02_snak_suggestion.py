#  for python input we have to use - input() function and we can also use .lower() method 
# to convert the input to lowercase for easier comparison for below case.

snack = input("Enter your preferred snack: ").lower()

if snack == "cookies" or snack == "samosa":
    print(f"Great Choice! We'll serve you {snack}")
else:
    print("Sorry, we only serve cookies or samosa with tea")