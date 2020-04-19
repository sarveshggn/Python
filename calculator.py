import sys

class Operation:
    def __init__(self, operation, numbers):
        self.operation = operation
        self.numbers = numbers

def introduction():
    print("    Python Calculator    \n\n")

def print_instructions():
    instructions = "Type your command in the format : "
    instructions += "add 1,2\n"
    instructions += "Possible operations: addition, substraction, multiplication, division"
    print(instructions)

def get_user_input():
    user_input = input("Enter your command: ")
    return user_input

def parse_input(user_input):
    user_input_parsed = user_input.split(" ")
    user_input_numbers = user_input_parsed[1].split(",")
    user_input_numbers_int = []
    for number in user_input_numbers:
        user_input_numbers_int.append(int(number))
    operation = Operation(user_input_parsed[0], user_input_numbers_int)
    return operation

def run_operation(task):
    if task.operation == "add":
        answer = task.numbers[0]
        numbers = task.numbers[1:]
        for number in numbers:
            answer += number
        return answer

    if task.operation == "subtract":
        answer = task.numbers[0]
        numbers = task.numbers[1:]
        for number in numbers:
            answer -= number
        return answer

    if task.operation == "multiply":
        answer = task.numbers[0]
        numbers = task.numbers[1:]
        for number in numbers:
            answer *= number
        return answer

    if task.operation == "divide":
        answer = task.numbers[0]
        numbers = task.numbers[1:]
        for number in numbers:
            answer /= number
        return answer

def answer_user(solution):
    answer = "\nYour answer is: "
    answer += str(solution)
    answer += "\n"
    print(answer)

def ask_again():
    again = input("Would you like to enter another command? ")
    if again[0].lower() == "y":
        return True
    if again[0].lower() == "n":
        sys.exit()

def main():
    while True:
        introduction()
        print_instructions()
        user_input = get_user_input()
        operation = parse_input(user_input)
        answer = run_operation(operation)
        answer_user(answer)
        ask_again()

main()

####################################################################
# def ask_again():                                                ##
#     again = input("Would you like to enter another command? ")  ##
#     if again[0].lower() == "y":                                 ##
#         return True                                             ##
#     if again[0].lower() == "n":                                 ##
#         return False                                            ##
#                                                                 ##
# def main():                                                     ##
#     again = True                                                ##
#     while again == True:                                        ##
#         introduction()                                          ##
#         print_instructions()                                    ##
#         user_input = get_user_input()                           ##
#         operation = parse_input(user_input)                     ##
#         answer = run_operation(operation)                       ##
#         answer_user(answer)                                     ##
#         again = ask_again()                                     ##
#                                                                 ##
# main()                                                          ##
####################################################################
