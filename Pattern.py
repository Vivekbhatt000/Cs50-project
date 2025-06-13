# Program to give out a pattern 
n = int(input('How many time should I repeat? '))

if n <= 0:
    print('Please enter a positive integer.')
else:
    for i in range(1,n + 1):
        print("*" * i)

