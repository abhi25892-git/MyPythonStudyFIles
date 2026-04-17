import MyModule as mm

print("1st program :", mm.welcome_msg.__doc__)
val1 = str(input("Enter the sex of the person : "))
val2 = str(input("Enter the marital status of the person : "))
val3 = str(input("Enter the name of the person : "))
mm.welcome_msg(val3, val1, val2)

print("2nd program :", mm.interest.__doc__)
val = int(input("Enter the principal amount : "))
mm.interest(val)

print("3rd program :", mm.square.__doc__)
val = int(input("Enter the number of elements in the list : "))
l2 = []
for j in range(val):
    ele = int(input("Enter the elements : "))
    l2.append(ele)
print("Elements before calling :", l2)
mm.square(l2)
print("Elements after calling :", l2)

print("4th program :", mm.palindrome.__doc__)
val1 = input("Enter a string : ")
pal = mm.palindrome(val1)
if pal is True:
    print("Palindrome")
else:
    print("Not palindrome")

print("5th program :", mm.factorial.__doc__)
val2 = int(input("Enter a number : "))
f = mm.factorial(val2)
print("Factorial is :", f)

print("6th program :", mm.areaperi.__doc__)
val3 = float(input("Enter the length of the rectangle : "))
val4 = float(input("Enter the breadth of the rectangle : "))
are, peri = mm.areaperi(val3, val4)
print(f"Area : {are} and Perimeter : {peri}")
