def hello() :
    # Ask user for their name 
    Name = input ("what's your name? ").title().strip()
    print('Hello,', Name)
  

Name = input ("what's your name? ")

# Capatalize user's first name
Name = Name.capitalize()
# Say hello using first name
first, last = Name.split()
print(f'hello, {first}')
# Capatalize user's name 
Name = Name.title()

# Remove extra space between charachters
Name = Name.strip()

# Remove extra space between charachters and Capatalize user's name 
Name = Name.strip().title()

 # Method 1
print(f'Hello, {Name}') 

#  Method 2
print('Hello,', Name)

# Method 3
print('Hello,', end= ' ')
print(Name)

# Method 4
print('Hello,',Name,sep=' ')

hello()