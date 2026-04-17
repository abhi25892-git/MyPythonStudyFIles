
def welcome_msg(name, sex, marital_status):
    """Display a welcome message according to the inputs"""
    if sex == 'Male':
        print("Welcome Mr.", name)
    elif sex == 'Female' and marital_status == 'Married':
        print("Welcome Mrs.", name)
    else:
        print("Welcome Miss.", name)


def interest(principal, rate=5, time=5):
    """Calculate the simple interest"""
    si = round((principal * rate * time)/100, 2)
    print("Your interest is :", si)


def square(l1):
    """Display the square of the list entered"""
    for i in range(len(l1)):
        l1[i] = l1[i] ** 2


def palindrome(n):
    """Checks whether a string entered is palindrome or not"""
    res = (n == n[::-1])
    return res


def factorial(n):
    """Calculate the factorial of a number"""
    for i in range(1, n):
        n = n * i
    return n


def areaperi(length, breadth):
    """Calculate the area and perimeter of a rectangle"""
    ar = round(length * breadth, 2)
    per = round(2 * (length + breadth), 2)
    return ar, per















