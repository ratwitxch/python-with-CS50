import math
# gets the package that has the square root function

def main():
    x = input("\nI AM MATH WIZARD!!\nGive me a number and I will square root it to the best of my abilities 0w0\n=> ")
    # asks user for a number

    x = float(x)
    # "floats" it ^ -^

    print("The square root of " + str(int(x)) + " is " + str(sq(x)) , end = ",\n")
    # shows the estimated square root

    print("with a remainder of " + str(int(rem(x))) , sep = "", end = ".\n")
    # shows the remainder

# function that contains all the instructions



def sq(num):
    num = math.floor(math.sqrt(num))
    return num

# square roots & rounds down the number

def rem(uh):
    uh = uh % sq(uh) ** 2
    return uh
# finds the remainder of the number by dividing with the square of the square root

main()
# calls the main function


'''
hehe now I have to import packages..
borrowing code is def much easier!
It reminds me,
you can always ask for help (;
'''