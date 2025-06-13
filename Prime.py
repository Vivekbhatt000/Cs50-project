# Program to check if a no. is prime or not                
x = int(input('Enter number: '))
y = []
if x <= 1:
    print(f'{x} is neither prime nor composite.') 

else:
    for i in range(1, x +1):    
        
        if x % i == 0:
            y.append(i)
    if len(y) > 2 :
        print(f'{x} is a composite no.')
    else:
        print(f'{x} is a prime no.')
