import random
def main():
    print("\nI'm sorta lazy rn..\nmind buying snacks for me?")
    print("\n> 1 | Sure, why not. Not like I have anything better to do.")
    print("> 2 | Beat it! You've got legs don't you?\n")
    mode = input("=> ")
    # gives two choices to choose how they continue the story

    if mode == "1":
        print("\n> Sure, why not. Not like I have anything better to do.")
        n = (random.randrange(11))
        input("\nthxx, ur the bezzt.")
        input("\n> So wa da yaa want?")
        input("\npocky..")
        input("\n> How many?")
        # chooses a random number from 1-9
        # tells the player to guess

        g = "0"
        print("\nprob less than 10, guess..")
        play(g)
        # gives instructions & calls the guessing function 

    else:
        print("\n> Beat it! You've got legs don't you?\n")
        quit()
        # quits the code if they input anything else than 1

def play(x):
    n = (random.randrange(1,10))
    # generates a random integer from 1-9

    while x != n:
        #  keeps looping until their guess is right
        x = str(input("=> "))
        if x.isdigit() == False:
            input("\nwut.. r you like high rnn.")
            # tells to guess again if they input smthg other than a number

        else:
            x = int(x)
            if x == n:
                print("\nyup, and you're payin for it!\n")
                quit()
                # ends loop if their guess is correct


            elif x > n:
                print("\nnah, unless you're having some too ofc")
            else:
                print("\nmy tummy wummy says more")
            # if their guess is too big or too small it will tell


main()

'''
went off track & made a little game ^ _^
inspired by my pocky addicted friend,
idk how it got this gudd but yayyyy!!
I reused some code from my number game
and made smthg fun out of it siluekgawifkb

used mostly input cuz i found out it lets you press enter to continue the story
'''