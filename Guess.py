
def get_guess():
    Guess = int(input('Type your guess number: '))
    return Guess

def main():
    Guess = get_guess()
    if Guess == 50:# The no. is understood as a string. So, use int        
          print('Correct!')
    else:
        print('Incorrect!')


main()



