def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def calculator():
    num1 = float(input("What is the first number? "))
    start_calc = True

    while start_calc:
        for operator, function in operations.items():
            print(operator)

        define_operator = input("Pick an operator from the line above: ")
        num2 = float(input("What is the next number? "))

        for operator, func in operations.items():
            if operator == define_operator:
                operation = func

        answer = operation(num1, num2)
        print(f"{num1} {define_operator} {num2} = {answer}")

        continue_calc = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start again: ")

        if continue_calc == "y":
            num1 = answer
        else:
            start_calc = False
            calculator()


calculator()
