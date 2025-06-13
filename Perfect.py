# Program to find if a no. perfect or not
divisor = []
n = int (input('Enter no.: '))
for i in range(1,n):
    if n % i == 0 :
        divisor.append(i)
sumd = sum(divisor)
        
if n <= 0:
    print('Enter a positive no.')

elif( sumd == n):
    print(f'{n} is a perfect no.')


else:
    print(f'{n} is not a perfect no.')

