#Program to give out largest no.
a,b,c = int(input('Enter no.1: ')),int(input('Enter no.2: ')),int(input('Enter no.3: '))
if a>b>c or a>c>b:
    print(f'{a} is largest')
elif b>a>c or b>c>a:
    print(f'{b} is largest')
elif c>a>b or c>b>a:
    print(f'{c} is largest') 
