'''results = ['Mario', 'Luigi','']
results.append('Princess')
results.append('Yoshi')
results.append('Koopa Troopa')
results.append('Toad')
results.append(['Bowser', 'Donkey Kong Jr.'])
results.remove(['Bowser', 'Donkey Kong Jr.'])
results.extend(['Bowser', 'Donkey Kong Jr.'])

print(results)'''


results = ['Mario', 'Luigi', 'Princess', 'Bowser', 'Yoshi', 'Koopa Troopa', 'Toad', 'Donkey Kong Jr.' ]

results.remove('Bowser')
results.insert(0,'Bowser')
results.reverse()

print(results)
