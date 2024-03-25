def diff(a , b):
    a = float(a)
    b = float(b)
    # turns inputs into floats

    c = abs(a - b) 
    # finds the difference between the inputs

    print(f"And their difference is {c : .2f}")
    # prints & rounds result to 2 decimal points
    
x = input("\nThink of a number..\n=> ")
y = input("\nThink of another to go with it!\n=> ")
# asks user for 2 numbers

diff(x , y)
# runs diff function

'''
Coding gets complicated fast,
but take your time.
I luv CS50's course so far,
it gets interesting real quick!
'''