x = int(input('What\'s x? '))
y = int(input('What\'s y? '))

if x < y:
    print('x is less than y')
elif x > y :
    print('x is greater than y')
elif x == y :
    print('x is equal to y')
else:
    print(' x = y') 

if x < y or x > y: # or function
    print('x is not equal to y')
else :
    print('x is equal to y') 

if x != y:
    print('x is not equal to y')

else :
    print('x is equal to y') 