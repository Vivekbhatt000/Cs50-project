# Program to find Fabonacci series upto n terms
n = int(input('Enter the no. of terms of Fabonacci Series: ' ))
a = 0
b = 1
print ('Fabonacci Series-')
for i in range(1,n+1):
    print(a, end = ' ')
    nxt= a + b
    a = b 
    b = nxt
    nxt = a
print('')

terms = int(input('Enter the number of rows: '))
if terms <= 0 :
    print('Enter a positive integer')
else:    
    for num in range( terms, 0, -1):
        for i in range(1, num + 1):
            print (i,end =' ')
        print(' ')
