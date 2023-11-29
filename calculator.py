# now i am gonna show u a code of calculator by pyhton language

def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mult(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


def main():

    num1 = float(input("enter ur first value : "))
    operator = input("Enter any oparetor + , - , * , / : ")
    num2 = float(input("enter ur second value : "))

    if operator == "+":
        result = add(num1, num2)

    elif operator == "*":
        result = mult(num1, num2)

    elif operator == "-":
        result = sub(num1, num2)

    elif operator == "/":
        result = div(num1, num2)

    else:
        print("cheack koro vul ache")
        return

    print(f" {num1} {operator} {num2} = {result} ")


if __name__ == "__main__":
    main()

print("thanks a lot brudha <3")


