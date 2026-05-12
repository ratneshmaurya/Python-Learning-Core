# input() hamesha string return karta hai.

# Even agar user number likhe tab bhi.
age = input("Enter age: ")
print(type(age))


# for numvber input karna hai to hume usko int() me convert karna padega.
age = int(input("Enter age: "))
print(type(age))

# for float input karna hai to hume usko float() me convert karna padega.
price = float(input("Enter price: "))
print(type(price))

#  for 2inputs 
a, b = input("Enter two numbers: ").split()
print(a)
print(b)

#  -------------------- for multiple inputs
# map(int, ["1", "2"])
# Ye har element ko int me convert karta hai.

# Multiple integers - a, b = map(int, input().split())

# Space separated numbers - 
nums = list(map(int, input().split()))
print(nums)

#  list of ints - 
arr = list(map(int, input().split()))
print(arr)


# ------------------------ Input Conclusions -------------------------------
# String-input	    =>  input()
# Integer-input	    =>  int(input())
# Float-input	    =>  float(input())
# Multiple-values	=>  input().split()      space separated inputs diye hai user ne
# Multiple-ints	    =>  map(int, input().split())
# List of ints      =>	list(map(int, input().split()))
