# define the function needed (add, sub, mult, div)
# print option to the user
# ask for values
# call the function
# while loop to continue the program until the user wants to exit

def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")

def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")

def mult(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")

def div(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")

while True:
    print("A. Addition")
    print("B. Substraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("input yor choice: ")

    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("input your first number: "))
        b = int(input("input your second number: "))
        add(a, b)
    elif choice == "b" or choice == "B":
        print("Substraction")
        a = int(input("input your first number: "))
        b = int(input("input your second number: "))
        sub(a, b)
    elif choice == "c" or choice == "C":
        print("Multiplication")
        a = int(input("input your first number: "))
        b = int(input("input your second number: "))
        mult(a, b)
    elif choice == "d" or choice == "D":
        print("Division")
        a = int(input("input your first number: "))
        b = int(input("input your second number: "))
        div(a, b)
    elif choice == "e" or choice == "E":
        print("Program ended")
        quit()
