def main ():
    history = []
    
    while True:
        action = input('Action: ')
    
        if action == 'Undo':
            undone = history.pop()  # Removes the last added element in list   
            print(f'Undone: {undone}')
        
        elif action == 'Restart':
            history.clear()  # clears the whole data in the list
        
        else:
            history.append(action)
        
        print(history)
    



main()