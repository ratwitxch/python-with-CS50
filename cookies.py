def main():
    print("-------------------------------------------------------")
    input("\nYou're baking cookies today!")
    print("The amount you bake will decide who you'll share it with.")
    print("\nHow many will you bake?")
    cookies = input("\n=> ")
    share(cookies)


def share(x):
    while x.isdigit() != True:
        x = input("\nThat ain't a number silly!\n=> ")
    
    x = int(x)
    if x == 0:
        input("\nLooks like no one's getting cookies T - T\n")
    
    elif x == 1:
        input("\nIt'll be DA 'PERFECT' cookie  ~~旦_(- ω-｀｡)\n")
    elif 1 < x <= 10:
        input("\nIt's all for me this time <;\n")

    elif 10 < x <= 30:
        input("\nI'll give some to my bestiezz \n& have them praise my baking skills uwu\n")

    elif 30 < x <= 100:
        input("\nThis should be enough to feed the kids in the basement.. \n")
        
    else:
        input("\nIs that even possible?\nwhat am i saying.. OFC IT ISS\nLET'SS GO  ψ (｀∇´) ψ\n")

main() 



