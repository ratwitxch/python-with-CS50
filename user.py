def greet(to = "world"):
    print("\nIt's my pleasure ", to , "!\n" , sep = "")
    # greets user with their name

user = input("\nWhat may I call you?\n=> ")
# asks user for name

user = user.strip().title()
# gets rid of spaces
#capitalizes first letter of each word

greet(user)

"""
Feel free to edit! O w O
This is my beginner but not really code.
My first code in relearning Python basics,
with CS50's Python course!
"""