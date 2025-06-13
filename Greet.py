# using print function

def greet(input):
    if 'hello' in input:
        print('Hello, there')
    else:
        print("I am not sure what you mean")

greet("hello")

# using return function
def greet(input):
    if 'hello' in input:
        return 'Hello, there'
    else:
        return "I am not sure what you mean"

greeting =  greet('hi') # Have to use a variable also
print(greeting)

