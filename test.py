import sys
print(sys.version)
def triangle(z):
    z = int(input("How tall do you want your triangle to be? "))
    y = input("Enter your preferred character: ")
    for i in range(1, z + 1):
        print(y * i)
triangle(10)
# def flip(x):
#     for i in range(100, x - 1):
#         print("*" * i)
# flip(123)
def bismillahjalan(z):
    z = int(input("How tall do you want your triangle to be? "))
    y = input("Enter your preferred character: ")
    for i in range(z, 0, - 1):
        character = y
        print(y * i)
bismillahjalan(10)
def bismillah(z):
    z = int(input("How tall do you want your triangle to be? "))
    y = input("Enter your preferred character: ")
    for i in range(z, 0, -1):
        character = y
        space = " "
        print((space * (z - i)) + (y * i))
bismillah(10)