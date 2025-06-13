name = input('What\'s your name? ')

if name == "Haryy" or 'Ron' or 'Hermonie': # using or function
    print ('Gryffindor')
elif name == 'Ron':
    print ('Gryffindor')
elif name == 'Hermonie':
    print ('Gryffindor')
elif name == 'Draco':
    print ('Slytherin')
else:
    print('Who?')
# code doesn't work due to outdated python version used
match name:
    case 'Harry' | "Ron" | 'Hermione': # | similar to or function 
        print('Gryffindor')
    case _: # '_' case not handeled similar to else function
        print('Who?')    