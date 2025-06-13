def main():
        x = int(input("What's x? "))
        if  is_even(x): 
            print('Even')
        else:
                print('Odd')

def is_even(x):
        if x % 2 == 0 :
         return True 
        else: 
                return False        
 
        return True if x % 2 == 0 else False  # compiling is_even in single line
        return (x % 2 == 0 )
        
                
main()
x = int(input('What\'s your number? ' ))

if x % 2 == 0 :
        print('Even')
else: 
        print('Odd')
