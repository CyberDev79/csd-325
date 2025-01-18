"""Cho-Han, by Al Sweigart al@inventwithpython.com
The traditional Japanese dice game of even-odd.
View this code athttps://nostarch.com/big-book-small-python-projects
Tags: short, beginner, game"""

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

# 3. In the program introduction, include a notice that if the user gets a 2 or a 7 on a dice roll, they get a 10 mon bonus.
print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number. If the total of the
two dice equal a 2 or 7 the player gets a 10 mon bonus.
''')

# 1. Change the input prompt to your initials and a colon. Ex. mss:
prompt = "jdm: "


purse = 5000
while True:  # Main game loop.
    # Place your bet:
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        pot = input(prompt)
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            # This is a valid bet.
            pot = int(pot)  # Convert pot to an integer.
            break  # Exit the loop once a valid bet is placed.

    # Roll the dice.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Let the player bet cho or han:
    while True:
        bet = input(prompt).upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    # Reveal the dice results:
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # 4. If the dice roll is equal to a 2 or a 7, output a message to the user what the total of roll was and that they got a 10 mon bonus. Then add that bonus to the purse.
    bonus = 0
    dice_sum = dice1 + dice2
    while True:
        if dice_sum == 2:
            bonus = 10
            print(f"\nCongrats on rolling a {dice_sum}, you will get an 10 mon bonus regardless if you win or lose!\n")
            break
        elif dice_sum == 7:
            bonus = 10
            print(f"\nCongrats on rolling a {dice_sum}, you will get an 10 mon bonus regardless if you win or lose!\n")
            break
        else:
            bonus = 0
            print(f"\nYour total was {dice_sum}. Since it didn't equal a 2 or 7 so you didn't earn a 10 mon bonus on this role\n")
            break

    # Determine if the player won:
    rollIsEven = (dice1 + dice2) % 2 == 0
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    # Display the bet results:
    # 2. Change the percentage that goes to the house to 12 percent instead of 10 percent.
    # I tested this and bet 1000 and won, the dealer took $83 instead of $120 due to how python rounds down
    # I created a dealer_fee calculation and referenced that variable dealer_fee
    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse = purse + pot + bonus  # Add the pot from player's purse.
        dealer_fee = int(pot * 0.12) # You can change the dealer fee from 12% (0.12) to any value here
        print('The house collects a', dealer_fee, 'mon fee.')
        purse = purse - dealer_fee  # The house fee is 12%.
    else:
        purse = purse - pot + bonus  # Subtract the pot from player's purse.
        print('You lost!')

    # Check if the player has run out of money:
    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()
