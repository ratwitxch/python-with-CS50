x = input("\nThink of a number..\n=> ")
y = input("\nThink of another to go with it!\n=> ")

# asks user for 2 numbers

x = float(x)
y = float(y)

# turns inputs into integers

z = x + y 
a = abs(x - y) 
# adds the inputs 
# decreases & finds the absolute value of the inputs

z = round(z , 2)
print("\nAdding them, we get " + str(z), end = "\n\n")
# print(f"\nAdding them,we get {z : .2f}")

a = round(a , 2)
print("And their difference is " + str(a))

# print(f"And their difference is {a : .2f}")

# rounds result to 2 decimal points
# prints the resulting calculations


'''
Coding gets complicated fast,
but take your time.
I luv CS50's course so far,
it gets interesting real quick!
'''