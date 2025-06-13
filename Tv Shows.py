


Shows = [
    'Ben 10',
    ' pokemon',
    'courage the cowardly dog',
    '  the Adventure time',
    '    dora the Explorer'
]

def main():
    for show in Shows:
        print(show.strip().title())
 # Strip() function removes unnecessary spaces between words
 # title() function capatalize every single first word 
 # capatalize() function capatalize only fist word
main()

def another():
    cleaned_shows = []
    for show in Shows:
        cleaned_shows.append(show.strip().title())

    print(', '.join(cleaned_shows))

another() 