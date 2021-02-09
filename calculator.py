def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def multi(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": sub,
    "*": multi,
    "/": div
}


def calculator():
    num1 = int(input("What is the first number: "))
    for ops in operations:
        print(ops)
        should_continue = True

    while should_continue:
        ops_symbol = input("Enter an operation symbol: ")
        num2 = int(input("What is the next number: "))
        cal = operations[ops_symbol]
        answer = cal(num1, num2)
        print(f"{num1} {ops_symbol} {num2} = {answer}")

        if input("Do you want to continue? Press y else n: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()

