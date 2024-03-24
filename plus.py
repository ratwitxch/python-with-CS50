def plus(a , b):
    a = float(a)
    b = float(b)
    # turns inputs into floats

    c = a + b 
    # adds the inputs

    print(f"\nAdding them,we get {c : .2f}")
    # prints & round result to 2 decimal points
    
x = input("\nThink of a number..\n=> ")
y = input("\nThink of another to go with it!\n=> ")
# asks user for 2 numbers

plus(x , y)
# runs plus function

'''
Coding gets complicated fast,
but take your time.
I luv CS50's course so far,
it gets interesting real quick!
'''