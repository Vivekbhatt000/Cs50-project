
emoticon = 'v.v' # Depicts sad mood

def main():
    global emoticon
    say('Is anyone there?')
    
    emoticon = ':)'
    say('Oh, Hi')

def say(phrase):
    print(phrase+" "+emoticon)

main()