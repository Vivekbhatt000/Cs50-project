WORDS = {'PAIR': 4, 'HAIR': 4, 'CHAIR': 5, 'Graphic': 7}

def main():
    print('Welcome to spelling Bee!')
    for word, point in WORDS.items():
       print(f'{word} was worth {point} points.') 

    print('Your letters are: A I P C R H G')
    while len(WORDS) > 0:
        print(f'{len(WORDS)} words left!')
        guess = input('Guess a word: ')

        # TODO: Check if  guess in dictionary
        if guess == 'Graphic':
            WORDS.clear()
            print('You\'ve won')
        
        if guess in WORDS.keys():
            POINTS = WORDS.pop(guess)
            print(f'Good job! You scored {POINTS} points.')
        
    print('That\'s the game!')


main()