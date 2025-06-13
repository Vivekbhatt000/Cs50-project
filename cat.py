x = 2
while x != 0:
    print('meow')
    x = x - 1

i = 0
while i < 2:
    print('meo')
    i += 1 # or i = i +      

for i  in [0, 1]:
    print('me')

for i in range(2):
    print('m')

print('meow\n' * 3, end = '')

# asking user to meow

while True :
    n = int(input('What\'s n? ' ))
    if n > 0 :
        break 

for _ in   range(n):
    print('meo')

def main():
    meow(n)

def meow(n):
    n = int(input("What's n? "))
    for _ in range(n):
        print('meow') 
    
main()