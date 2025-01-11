# Name: Justin Morrow
# Date: 01/10/2025
# Assignment: CSD325 Module 1.3 "On the Wall"
# Purpose: Use a function to iterate through an input value representing how many bottles of beer are on the wall.
# Reference: W3Schools. (n.d.). Python string format method. W3Schools. Retrieved January 11, 2025, from https://www.w3schools.com/python/ref_string_format.asp
# Reference: GeeksforGeeks. (n.d.). Python range() function. GeeksforGeeks. Retrieved January 11, 2025, from https://www.geeksforgeeks.org/python-range-function/

"""Ask the user how many bottles of beer are on the wall.
Pass that input to a function that manages the countdown.
The function should take the input and count backwards to 1 while displaying the number of remaining bottles of beer on the wall.
Once the count is down to 1, change lyrics to show "1 bottle of beer..."
At the end of the countdown, get back to the main program and remind the user to buy more beer."""

# Emoji Hed/Dec lookup site: https://symbl.cc/en/unicode-table/
beer_emoji = chr(127866)
drunk_emoji = chr(129326)
music_emoji = chr(127925)

print (f"Lets play Americas favorite drinking game... {beer_emoji}\n")
print ("Don't worry if you can't sing, you'll improve after every round!\n")

# Song verses - Using {} as a placeholder for input bottles value
verse1 = "{} bottle(s) of beer on the wall "
verse2 = "{} bottle(s) of beer "
verse3 = "take one down and pass it around "
verse4 = "0 bottles of beer on the wall.\n\nTime to buy more bottles of beer.\n"


def main():
    while True:
        try:
            choice = input("Ready to have some fun? Y/N: ").strip().upper()
            if choice == "Y":
                while True:
                    try:
                        bottles = int(input(f"\nHow many bottles of beer {beer_emoji} do you want to put on the wall? "))
                        if 1 <= bottles < 10:
                            print("\nYou're a lite weight, this should go quickly\n")
                        elif 10 <= bottles < 50:
                            print("\nYou've played this game before, this should be fun\n")
                        elif bottles > 50:
                            print("\nYou're a party animal, I'll try to keep up!\n")
                        else:
                            print("\nYou didn't enter a valid number of bottles. Enter the number of bottles (Ex: 1, 10, 25, 50, 75, 99, 100)\n")
                            break
                        print("\nLet's begin...\n")
                        for i in range(bottles, 0, -1): # range(start, stop, step)
                            print(f"{music_emoji}",verse1.format(i))
                            print(f"{music_emoji}",verse2.format(i))
                            print(f"{music_emoji}",verse3)
                            print()
                        print(f"{music_emoji}",verse4)
                        break
                    except ValueError:
                        print("\nHow many beers have you had? You didn't enter a correct response. Please try again.\n")
            elif choice == "N":
                print(f"\nIt's almost last call anyway and you don't look so good. {drunk_emoji} I'll get you an Uber home.\n")
                break
            else:
                print("\nYou didn't enter a valid input. Enter Y to start the party and N to quit\n")
        except ValueError:
            print("\nSomething went wrong. Please try again\n")


if __name__ == "__main__":
    main()