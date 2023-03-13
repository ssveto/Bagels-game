#Bagels, a deducive logic game where you have to guess a number based on clues.

import random

num_digits = 3 # number of digits to guess
max_guesses = 10 # number of guesses

def main():
    print(''' Bagels is a deductive logic game.
    
I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. The clues are :
When I say:     That means:
Pico            One digits is correct but in the wrong position.
Fermi           One digit is correct and in the right position.
Bagels          No digit is correct.

Example: If the secret number is 248 and your guess was 843, the cluess would be Fermi Pico.'''.format(num_digits))

    while True: # Main game loop
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print('You have {} guesses to get it'.format(max_guesses))

        numGuesses = 1
        while numGuesses <= max_guesses:
            guess = ''
            # Keep looping until they enter a valid guess.
            while len(guess) != num_digits or not guess.isdecimal():
                print('Guess #{}'.format(numGuesses))
                guess = input('> ')
            
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > max_guesses:
                print('You ran out of guesses.')
                print('The answer was {}'.format(secretNum))

        # Asking player if they want to play again.
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')


def getSecretNum():
    """ Returns a string made up of num_digits unique random digits."""
    numbers = list('0123456789') # Create a list of digits 0 to 9
    random.shuffle(numbers) # shuffle them into random order

    secretNum = ''
    for i in range(num_digits):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    """returns a string with the pico, fermi, bagels clues for guess 
    and secret number pair"""
    if guess == secretNum:
        return 'You got it!'
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct digit is in the correct place.
            clues.append('Fermi ')
        elif guess[i] in secretNum:
            # A correct digit is in the incorrect place.
            clues.append('Pico ')
    if len(clues) == 0:
        return 'Bagels' # No correct digits at all.
    else:
        # Sorting the clues into alphabetical order so their 
        # original order doesn't give information away.
        clues.sort()
        return ''.join(clues)
    

# if the program is run (instead of imported), run the game:
if __name__ == '__main__':
    main()