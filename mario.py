def main():
    print_column(3)
def print_column(n):
    for _ in range(n):
    #   print('#') can be used
        print('#\n', end='')
main()


def hor():
    print_row(4)

def print_row(width):
        print('?' * width)

hor()

def sq():
    print_sq(3)

def print_sq(b):
    print('*\n' * b, end = '')

sq()



def print_sq(size):
# for each row
    for i in range(size):
        # for each brick in row
        for j in range(size):
            # print brick
            print('#', end ='')
        print()

print_sq(3)