
from art import logo
print(logo)

def add(n1, n2):
    return n1 + n2



# my_favourite_calculation = add
#
# print(my_favourite_calculation(3, 5) ) # Will return 8

#  Todo write out other 3 functions subtract multiply and divide

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1* n2

def divide(n1,n2):
    return n1/n2
operations = {"-":subtract,
              "*":multiply,
              "+":add,
              "/":divide,
}

# TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.


while True:
    number_1 = float(input("What's the first number?: "))
    user_input = input("+\n-\n*\n/\nPick an operation: ")
    next_number = float(input("What's the next number?: "))

    while True:
        if user_input in operations:
            cal_number = (operations[user_input](number_1,next_number))
            print(f"{number_1} {user_input} {next_number} = {cal_number}")
            number_1 = cal_number

            restart = input(f"Type 'y' to continue calculating with {cal_number}, or type 'n' to start a new calculation:")
            if restart =="n":
                print("\n"*20)
                break
            elif restart == "y":
                user_input = input("+\n-\n*\n/\nPick an operation: ")
                next_number = float(input("What's the next number?: "))



