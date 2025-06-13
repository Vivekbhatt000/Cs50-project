students = ['Hermione', 'Harry' , 'Ron']

print(students[0])
print(students[1])
print(students[2])


for s in students :
    print(s)


for i in range(len(students)):
    print(i + 1, students[i])   
student = {
    'Hermione': 'Gryffindor',
    'Haryy' : 'Gryffindor',
    'Ron' : 'Gryffindor',
    'Draco' : 'Slytherin',
}

print(student['Hermione']) 

for learner in student:
    print(learner, student[learner], sep = ', ')


name = [
    {'name' : 'Hermione', 'house': 'Gryffindor','patronus': 'Otter'},
    {'name' : 'Harry', 'house': 'Gryffindor','patronus': 'Stag'},
    {'name' : 'Ron', 'house': 'Gryffindor','patronus': 'Jack Russell terrier'},
    {'name' : 'Draco', 'house': 'Slytherin','patronus': None}
]

for s in name :
    print(s['name'], s['house'], s['patronus'], sep=', ')


